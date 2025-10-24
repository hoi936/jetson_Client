<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.*,model.MayDietCo,model.PhienHoatDong" %>
<%
    MayDietCo may = (MayDietCo) request.getAttribute("may");
    List<PhienHoatDong> phienList = (List<PhienHoatDong>) request.getAttribute("phienList");
%>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Chi tiết máy <%= may.getTenMay() %></title>
    <link rel="stylesheet" href="<%= request.getContextPath() %>/frontend/css/may_list.css">
</head>
<body>
    <div class="container">
        <header class="page-header">
            <h1>Chi tiết Máy diệt cỏ</h1>
            <div class="top-buttons">
                <a href="<%= request.getContextPath() %>/may-list" class="btn btn-view">← Quay lại danh sách</a>
                <a href="<%= request.getContextPath() %>/logout" class="btn btn-logout">Đăng xuất</a>
            </div>
        </header>

        <div class="machine-detail">
            <h2><%= may.getTenMay() %></h2>
            <p><b>Mã định danh:</b> <%= may.getMaDinhDanh() %></p>
            <p><b>Trạng thái:</b> 
                <span class="<%= "Đang hoạt động".equals(may.getTrangThai()) ? "status-on" : "status-off" %>">
                    <%= may.getTrangThai() %>
                </span>
            </p>

            <form method="post" action="<%= request.getContextPath() %>/may-detail?id=<%= may.getMaMay() %>" class="control-buttons">
                <button type="submit" name="action" value="START" class="btn btn-add">Bật máy</button>
                <button type="submit" name="action" value="STOP" class="btn btn-delete">Tắt máy</button>
            </form>
        </div>

        <h3>Danh sách các phiên hoạt động</h3>
        <table class="machine-table">
            <thead>
                <tr>
                    <th>Mã phiên</th>
                    <th>Thời gian bắt đầu</th>
                    <th>Thời gian kết thúc</th>
                    <th>Hành động</th>
                </tr>
            </thead>
            <tbody>
                <%
                    if (phienList != null && !phienList.isEmpty()) {
                        for (PhienHoatDong phien : phienList) {
                %>
                <tr>
                    <td><%= phien.getMaPhien() %></td>
                    <td><%= phien.getThoiGianBat() %></td>
                    <td><%= phien.getThoiGianTat() != null ? phien.getThoiGianTat() : "Đang hoạt động" %></td>
                    <td>
                        <a href="<%= request.getContextPath() %>/lich-su-phien?maPhien=<%= phien.getMaPhien() %>&maMay=<%= may.getMaMay() %>" class="btn btn-view">
                            Xem chi tiết
                        </a>
                    </td>
                </tr>
                <%
                        }
                    } else {
                %>
                <tr>
                    <td colspan="4" class="no-data">Chưa có phiên hoạt động nào.</td>
                </tr>
                <%
                    }
                %>
            </tbody>
        </table>
    </div>
</body>
</html>
