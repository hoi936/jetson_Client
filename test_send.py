import requests
import datetime
print("Bắt đầu gửi dữ liệu...")
# Địa chỉ IP của máy đang chạy Tomcat (đúng như khi em truy cập trên điện thoại)
url = "http://192.168.1.247:8080/may_diet_co/api/upload-lich-su" 
# Tạo dữ liệu giả để test
data = {
    "ma_lich_su":4,
    "ma_dinh_danh": "JETSON004",
    "so_co_phat_hien": 6,
    "so_co_diet": 5,
    "vi_tri": "123",
    "thoi_gian": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "ma_phien": 5
}

# Ảnh test (em thay đường dẫn ảnh thực tế)
files = {"anh": open("D:/PHAN ĐÌNH HỒI/PBL4/abc.png", "rb")}

# Gửi POST request
response = requests.post(url, data=data, files=files)

# In kết quả trả về từ server
print(response.status_code)
print(response.text)
files["anh"].close()  # Đóng file sau khi gửi