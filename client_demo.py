import socket
import threading
import time
import random

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
MAY_ID = "JETSON004" 

# --- Biến toàn cục để quản lý trạng thái ---
# Dùng threading.Event để báo hiệu cho luồng công việc dừng lại
g_stop_event = threading.Event() 
# Dùng Lock để bảo vệ 2 biến 'trang_thai' và 'current_task'
g_lock = threading.Lock()
g_trang_thai = "NGUNG_HOAT_DONG"
# (ma_phien, quang_duong_muc_tieu, quang_duong_hien_tai)
g_current_task = (None, 0, 0) 


def cap_nhat_trang_thai(new_status):
    """Hàm an toàn để cập nhật trạng thái (thread-safe)"""
    global g_trang_thai
    with g_lock:
        g_trang_thai = new_status
        print(f"🔄 Cập nhật trạng thái: {g_trang_thai}")

def gui_trang_thai(sock):
    """
    Luồng này CHỈ gửi trạng thái 3 giây 1 lần
    """
    while True:
        try:
            current_status = ""
            with g_lock:
                current_status = g_trang_thai
                
            msg = f"STATUS:{current_status}\n"
            sock.sendall(msg.encode('utf-8'))
            # print(f"📤 Gửi: {msg.strip()}") # Bỏ comment nếu muốn xem chi tiết
            time.sleep(3)
        except Exception as e:
            print(f"⚠️ Lỗi gửi trạng thái: {e}")
            break

def chay_nhiem_vu(sock, ma_phien, quang_duong_muc_tieu):
    """
    Một luồng riêng biệt mô phỏng máy đang chạy.
    Sẽ tự dừng khi đủ quãng đường, hoặc bị dừng bởi g_stop_event.
    """
    global g_current_task
    
    print(f"🚜 Bắt đầu Phiên {ma_phien}. Mục tiêu: {quang_duong_muc_tieu}m")
    cap_nhat_trang_thai("DANG_HOAT_DONG")
    
    q_hien_tai = 0
    q_muc_tieu = quang_duong_muc_tieu
    
    while q_hien_tai < q_muc_tieu:
        # Kiểm tra xem có bị server ra lệnh "STOP" không
        if g_stop_event.is_set():
            print(f"🛑 Nhận lệnh Dừng Thủ Công. Dừng ở {q_hien_tai}m")
            # Báo cáo quãng đường đã dừng
            msg = f"STOPPED:{q_hien_tai:.1f}\n"
            sock.sendall(msg.encode('utf-8'))
            break # Thoát khỏi vòng lặp
        
        # 1. Mô phỏng máy đang chạy
        time.sleep(2) # 2 giây chạy được 1 mét
        q_hien_tai += 1
        with g_lock:
            g_current_task = (ma_phien, q_muc_tieu, q_hien_tai)
        
        print(f"...Đang chạy phiên {ma_phien}: {q_hien_tai}m / {q_muc_tieu}m")

        # 2. Mô phỏng gửi dữ liệu cỏ
        if random.randint(1, 5) == 1: # 20% cơ hội tìm thấy cỏ
            try:
                vi_tri = f"{q_hien_tai + 0.5}, -12.3"
                so_co_diet = random.randint(1, 3)
                anh = f"img/phien_{ma_phien}_{q_hien_tai}.jpg"
                
                # Gửi WEED:
                weed_msg = f"WEED:{ma_phien}:{vi_tri}:{so_co_diet}:{anh}\n"
                print(f"🌿 Phát hiện cỏ! Gửi: {weed_msg.strip()}")
                sock.sendall(weed_msg.encode('utf-8'))
            except Exception as e:
                print(f"⚠️ Lỗi gửi WEED: {e}")

    # 3. Kết thúc
    with g_lock:
        # Reset task
        g_current_task = (None, 0, 0)
        
    if not g_stop_event.is_set():
        # Nếu không phải do STOP thủ công, nghĩa là nó TỰ HOÀN THÀNH
        q_thuc_te = q_hien_tai + random.uniform(0, 0.2) # Chạy lố 1 chút
        print(f"🏁 Hoàn thành Phiên {ma_phien}. Quãng đường thực tế: {q_thuc_te:.1f}m")
        msg = f"COMPLETED:{q_thuc_te:.1f}\n"
        sock.sendall(msg.encode('utf-8'))
    
    # Dù là COMPLETED hay STOPPED, cuối cùng đều là NGUNG_HOAT_DONG
    cap_nhat_trang_thai("NGUNG_HOAT_DONG")
    g_stop_event.clear() # Xóa cờ "STOP" để chuẩn bị cho lệnh tiếp theo


def nhan_lenh(sock):
    """
    Luồng này chịu trách nhiệm LẮNG NGHE LỆNH
    và KHỞI ĐỘNG/DỪNG luồng công việc.
    """
    buffer = ""
    current_task_thread = None # Luồng chạy nhiệm vụ
    
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                print(f"⚠️ Server đã đóng kết nối.")
                break
            
            buffer += data
            
            while '\n' in buffer:
                line, buffer = buffer.split('\n', 1)
                if not line:
                    continue
                
                print(f"📥 Nhận lệnh: {line}")
                
                # ✅ LỖI ĐÃ SỬA Ở ĐÂY
                if line.startswith("START:"):
                    # Lệnh: "START:<ma_phien>:<quang_duong>"
                    # Ví dụ: "START:83:20.0"
                    if current_task_thread and current_task_thread.is_alive():
                        print("⚠️ Cảnh báo: Vẫn đang chạy nhiệm vụ cũ, bỏ qua lệnh START mới.")
                        continue
                        
                    try:
                        parts = line.split(':')
                        ma_phien = int(parts[1])
                        # Xử lý dấu phẩy (,) thành dấu chấm (.)
                        quang_duong_muc_tieu = float(parts[2].replace(',', '.')) 
                        
                        g_stop_event.clear() # Đảm bảo cờ STOP đã tắt
                        
                        # Khởi động 1 luồng mới để chạy nhiệm vụ
                        current_task_thread = threading.Thread(
                            target=chay_nhiem_vu, 
                            args=(sock, ma_phien, quang_duong_muc_tieu), 
                            daemon=True
                        )
                        current_task_thread.start()
                        
                    except Exception as e:
                        print(f"⚠️ Lỗi phân tích lệnh START: {e}")

                elif line == "STOP":
                    # Lệnh dừng thủ công từ Server
                    print("Nhận lệnh STOP từ server... Báo hiệu cho luồng dừng lại.")
                    g_stop_event.set() # Bật cờ STOP
                    
        except Exception as e:
            print(f"⚠️ Mất kết nối khi nhận lệnh: {e}")
            g_stop_event.set() # Dừng luồng con nếu socket lỗi
            break

def main():
    while True:
        try:
            print("🔌 Đang kết nối tới server...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((SERVER_IP, SERVER_PORT))
            print(f"✅ Đã kết nối thành công tới {SERVER_IP}:{SERVER_PORT}")

            sock.sendall(f"MAY_ID:{MAY_ID}\n".encode('utf-8'))
            print(f"Đã gửi ID: {MAY_ID}")

            # Khởi động luồng gửi trạng thái
            thread_gui = threading.Thread(target=gui_trang_thai, args=(sock,), daemon=True)
            thread_gui.start()
            
            # Luồng chính lắng nghe lệnh
            nhan_lenh(sock)
            
        except Exception as e:
            print(f"⚠️ Không kết nối được server: {e}")
        finally:
            print("Đóng socket. Thử kết nối lại sau 5 giây...")
            sock.close() 
            g_stop_event.set() # Đảm bảo mọi luồng con đều dừng
            time.sleep(5)

if __name__ == "__main__":
    main()