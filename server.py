import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def handle_client(conn, addr):
    print(f"🔌 Kết nối từ {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"📩 Nhận từ {addr}: {data}")

            # Server có thể gửi phản hồi bật/tắt cho client ở đây
            if data == "REQUEST_STATUS":
                conn.send("DANG_HOAT_DONG".encode())  # ví dụ: server yêu cầu client bật
        except:
            break
    conn.close()
    print(f"❌ Mất kết nối với {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"🚀 Server đang lắng nghe tại {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
