<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.List,model.MayDietCo" %>
<%
    List<MayDietCo> listMay = (List<MayDietCo>) request.getAttribute("listMay");
%>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Danh sách Máy diệt cỏ</title>
    <link rel="stylesheet" href="<%= request.getContextPath() %>/frontend/css/may_list.css">
</head>
<body>
    <div class="container">
        <header class="page-header">
            <h1>Danh sách Máy diệt cỏ</h1>
            <div class="top-buttons">
                <a href="<%= request.getContextPath() %>/may-add" class="btn btn-add">+ Thêm máy mới</a>
                <a href="<%= request.getContextPath() %>/logout" class="btn btn-logout">Đăng xuất</a>
            </div>
        </header>

        <table class="machine-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Mã định danh</th>
                    <th>Tên máy</th>
                    <th>Trạng thái</th>
                    <th>Lần cuối hoạt động</th>
                    <th>Hành động</th>
                </tr>
            </thead>
            <tbody>
                <%
                    if (listMay != null && !listMay.isEmpty()) {
                        for (MayDietCo m : listMay) {
                %>
                <tr>
                    <td><%= m.getMaMay() %></td>
                    <td><%= m.getMaDinhDanh() %></td>
                    <td><%= m.getTenMay() %></td>
                    <td><%= m.getTrangThai() %></td>
                    <td><%= m.getLanCuoiHoatDong() %></td>
                    <td class="actions">
                        <a href="<%= request.getContextPath() %>/may-detail?id=<%= m.getMaMay() %>" class="btn btn-view">Chi tiết</a>
                        <a href="<%= request.getContextPath() %>/may-edit?id=<%= m.getMaMay() %>" class="btn btn-edit">Sửa</a>
                        <a href="<%= request.getContextPath() %>/may-delete?id=<%= m.getMaMay() %>"
                           class="btn btn-delete"
                           onclick="return confirm('Bạn có chắc muốn xóa máy này không?');">Xóa</a>
                    </td>
                </tr>
                <%
                        }
                    } else {
                %>
                <tr>
                    <td colspan="6" class="no-data">Không có máy nào trong danh sách</td>
                </tr>
                <%
                    }
                %>
            </tbody>
        </table>
    </div>
</body>
</html>
