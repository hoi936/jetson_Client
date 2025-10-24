<%@ page contentType="text/html;charset=UTF-8" %>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Đăng ký tài khoản</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/frontend/css/register.css">
</head>
<body>
    <div class="container">
        <div class="page-header">
            <h1>Tạo tài khoản mới</h1>
            <div class="header-buttons">
                <a href="${pageContext.request.contextPath}/login" class="btn btn-back">Quay lại</a>
            </div>
        </div>

        <form method="post" action="${pageContext.request.contextPath}/register" class="register-form">
            <div class="form-group">
                <label for="username">Tên đăng nhập</label>
                <input type="text" id="username" name="username" placeholder="Nhập tên đăng nhập..." required>
            </div>

            <div class="form-group">
                <label for="password">Mật khẩu</label>
                <input type="password" id="password" name="password" placeholder="Nhập mật khẩu..." required>
            </div>

            <div class="form-buttons">
                <button type="submit" class="btn btn-submit">Đăng ký</button>
                <a href="${pageContext.request.contextPath}/login" class="btn btn-cancel">Hủy</a>
            </div>
        </form>
    </div>
</body>
</html>
