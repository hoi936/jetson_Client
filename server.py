import socket
import threading
import time

SERVER_IP = "127.0.0.1"  # Địa chỉ IP của server Java
SERVER_PORT = 5000       # Cổng server Java đang lắng nghe
MA_DINH_DANH = "JETSON004"  # Mã định danh thiết bị
trang_thai = "STOP"  # Trạng thái mặc định

def nhan_lenh(sock):
    global trang_thai
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg == "START":
                trang_thai = "START"
            elif msg == "STOP":
                trang_thai = "STOP"
        except:
            print("🚫 Mất kết nối khi nhận lệnh.")
            break

def gui_trang_thai(sock):
    global trang_thai
    while True:
        try:
            msg = f"{MA_DINH_DANH} STATUS: {trang_thai}"
            sock.send(msg.encode())
        except:
            print("🚫 Mất kết nối khi gửi trạng thái.")
            break
        time.sleep(3)

def main():
    global trang_thai
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVER_IP, SERVER_PORT))
        print(f"✅ Đã kết nối tới server {SERVER_IP}:{SERVER_PORT}")
    except:
        print("🚫 Không thể kết nối tới server.")
        return

    # Gửi mã định danh thiết bị ngay sau khi kết nối
    try:
        sock.send(f"MAY_ID: {MA_DINH_DANH}\n".encode())
    except:
        print("🚫 Lỗi khi gửi mã định danh.")
        return

    # Bắt đầu các luồng gửi và nhận
    threading.Thread(target=nhan_lenh, args=(sock,), daemon=True).start()
    threading.Thread(target=gui_trang_thai, args=(sock,), daemon=True).start()

    # In trạng thái hiện tại mỗi 2 giây
    while True:
        print(f"📡 Trạng thái hiện tại: {trang_thai}")
        time.sleep(2)

if __name__ == "__main__":
    main()