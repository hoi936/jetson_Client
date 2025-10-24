<%@ page contentType="text/html;charset=UTF-8" %>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Thêm Máy diệt cỏ</title>
    <link rel="stylesheet" href="<%= request.getContextPath() %>/frontend/css/may-add.css">
</head>
<body>
    <div class="container">
        <header class="page-header">
            <h1>🌿 Thêm Máy diệt cỏ mới</h1>
            <div class="header-buttons">
                <a href="<%= request.getContextPath() %>/may-list" class="btn btn-back">←Quay lại danh sách </a>
                <a href="<%= request.getContextPath() %>/logout" class="btn btn-logout">Đăng xuất</a>
            </div>
        </header>

        <form action="<%= request.getContextPath() %>/may-add" method="post" class="add-form">
            <div class="form-group">
                <label for="maDinhDanh">Mã định danh:</label>
                <input type="text" id="maDinhDanh" name="maDinhDanh" required placeholder="Nhập mã định danh...">
            </div>

            <div class="form-group">
                <label for="tenMay">Tên máy:</label>
                <input type="text" id="tenMay" name="tenMay" required placeholder="Nhập tên máy...">
            </div>

            <div class="form-buttons">
                <button type="submit" class="btn btn-submit">💾 Thêm máy</button>
                <a href="<%= request.getContextPath() %>/may-list" class="btn btn-cancel">Hủy</a>
            </div>
        </form>
    </div>
</body>
</html>
