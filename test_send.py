import requests
import datetime
import time
import os

print("Bắt đầu gửi dữ liệu qua API...")

# ----------------- CẤU HÌNH -----------------
# Địa chỉ IP của máy đang chạy Tomcat
SERVER_IP = "192.168.1.247" # IP LAN của bạn
SERVER_PORT = "8080"
PROJECT_NAME = "may_diet_co"
API_ENDPOINT = "api/upload-lich-su"

url = f"http://{SERVER_IP}:{SERVER_PORT}/{PROJECT_NAME}/{API_ENDPOINT}" 

# Đường dẫn đến file ảnh bạn muốn test
IMAGE_PATH = "D:/PHAN ĐÌNH HỒI/PBL4/abc.png" # File ảnh này phải tồn tại

# Dữ liệu giả lập
# ✅ ĐÃ SỬA: Xóa 'ma_lich_su' và 'thoi_gian'.
# Server (CSDL) sẽ tự tạo 2 giá trị này.
data_payload = {
    "ma_dinh_danh": "JETSON004",
    "so_co_phat_hien": 8,
    "so_co_diet": 7,
    "vi_tri": "16.055, 108.223", # Gửi tọa độ GPS
    "ma_phien": "117" # Mã phiên nhận được từ lệnh START
}
# ---------------------------------------------

# Kiểm tra file ảnh có tồn tại không
if not os.path.exists(IMAGE_PATH):
    print(f"LỖI: Không tìm thấy file ảnh tại: {IMAGE_PATH}")
else:
    try:
        # Mở file ảnh ở chế độ đọc nhị phân ("rb")
        with open(IMAGE_PATH, "rb") as image_file:
            
            # Chuẩn bị file để gửi
            # "anh" là key mà Servlet @getPart("anh") mong đợi
            files_payload = {
                "anh": (os.path.basename(IMAGE_PATH), image_file, "image/png")
            }

            print(f"Đang gửi POST request đến: {url}")
            print(f"Dữ liệu (data): {data_payload}")
            print(f"File (files): {IMAGE_PATH}")

            # Gửi POST request, timeout 10 giây
            response = requests.post(url, data=data_payload, files=files_payload, timeout=10)

            # In kết quả trả về từ server
            print("--- KẾT QUẢ TỪ SERVER ---")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")

    except requests.exceptions.ConnectionError:
        print(f"LỖI: Không thể kết nối tới server tại {url}")
        print("Vui lòng kiểm tra địa chỉ IP và đảm bảo server Tomcat đang chạy.")
    except requests.exceptions.Timeout:
        print("LỖI: Request bị timeout (quá 10 giây)")
    except Exception as e:
        print(f"LỖI KHÁC: {e}")

print("--- Test script kết thúc ---")