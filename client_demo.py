import socket
import threading
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
MA_DINH_DANH = "JETSON004"

trang_thai = "NGUNG_HOAT_DONG"  # mặc định là dừng

def nhan_lenh(sock):
    global trang_thai
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg == "DANG_HOAT_DONG":
                trang_thai = "DANG_HOAT_DONG"
            elif msg == "NGUNG_HOAT_DONG":
                trang_thai = "NGUNG_HOAT_DONG"
        except:
            break

def gui_trang_thai(sock):
    global trang_thai
    while True:
        try:
            msg = f"{MA_DINH_DANH} STATUS: {trang_thai}"
            sock.send(msg.encode())
        except:
            print("🚫 Mất kết nối server.")
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

    threading.Thread(target=nhan_lenh, args=(sock,), daemon=True).start()
    threading.Thread(target=gui_trang_thai, args=(sock,), daemon=True).start()

    while True:
        print(f"📡 Trạng thái hiện tại: {trang_thai}")
        time.sleep(2)

if __name__ == "__main__":
    main()
