<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="model.MayDietCo" %>
<%
    MayDietCo may = (MayDietCo) request.getAttribute("may");
%>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Sửa Máy diệt cỏ</title>
    <link rel="stylesheet" href="<%= request.getContextPath() %>/frontend/css/may-edit.css">
</head>
<body>
    <div class="main-container">
        <div class="form-card">
            <h2 class="form-title">🛠️ Sửa thông tin máy</h2>

            <form action="<%= request.getContextPath() %>/may-edit" method="post" class="edit-form">
                <input type="hidden" name="id" value="<%= may.getMaMay() %>"/>

                <div class="form-group">
                    <label for="maDinhDanh">Mã định danh:</label>
                    <input type="text" id="maDinhDanh" name="maDinhDanh"
                           value="<%= may.getMaDinhDanh() %>" required>
                </div>

                <div class="form-group">
                    <label for="tenMay">Tên máy:</label>
                    <input type="text" id="tenMay" name="tenMay"
                           value="<%= may.getTenMay() %>" required>
                </div>

                <div class="form-group">
                    <label for="trangThai">Trạng thái:</label>
                    <select id="trangThai" name="trangThai">
                        <option value="DANG_HOAT_DONG" <%= "DANG_HOAT_DONG".equals(may.getTrangThai()) ? "selected" : "" %>>Đang hoạt động</option>
                        <option value="NGUNG_HOAT_DONG" <%= "NGUNG_HOAT_DONG".equals(may.getTrangThai()) ? "selected" : "" %>>Ngừng hoạt động</option>
                    </select>
                </div>

                <div class="btn-group">
                    <button type="submit" class="btn btn-submit">💾 Cập nhật</button>
                    <a href="<%= request.getContextPath() %>/may-list" class="btn btn-back">← Quay lại</a>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
