<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.*,model.LichSuCo,model.PhienHoatDong" %>
<%
    PhienHoatDong phien = (PhienHoatDong) request.getAttribute("phien");
    List<LichSuCo> lichSuList = (List<LichSuCo>) request.getAttribute("lichSuList");
%>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Lịch sử cỏ của phiên #<%= phien.getMaPhien() %></title>
    <link rel="stylesheet" href="<%= request.getContextPath() %>/frontend/css/may_list.css">
</head>
<body>
    <div class="container">
        <header class="page-header">
            <h1>Lịch sử cỏ của phiên #<%= phien.getMaPhien() %></h1>
            <a href="<%= request.getContextPath() %>/may-detail?id=<%= request.getAttribute("maMay") %>" class="btn btn-view">
                ← Quay lại chi tiết máy
            </a>
        </header>

        <div class="info-box">
            <p><b>Mã máy:</b> <%= phien.getMaDinhDanh() %></p>
            <p><b>Thời gian bắt đầu:</b> <%= phien.getThoiGianBat() %></p>
            <p><b>Thời gian kết thúc:</b> <%= phien.getThoiGianTat() != null ? phien.getThoiGianTat() : "Đang hoạt động" %></p>
        </div>

        <h3 style="color:#ff9800; margin-top:30px;">Dữ liệu phát hiện & diệt cỏ</h3>

        <table class="machine-table">
            <thead>
                <tr>
                    <th>Thời gian</th>
                    <th>Số cỏ phát hiện</th>
                    <th>Số cỏ diệt</th>
                    <th>Thứ tự</th>
                    <th>Ảnh minh họa</th>
                </tr>
            </thead>
            <tbody>
                <%
                    if (lichSuList != null && !lichSuList.isEmpty()) {
                        for (LichSuCo ls : lichSuList) {
                %>
                <tr>
                    <td><%= ls.getThoiGian() %></td>
                    <td><%= ls.getSoCoPhatHien() %></td>
                    <td><%= ls.getSoCoDiet() %></td>
                    <td><%= ls.getViTri() %></td>
                    <td>
                        <% if (ls.getDuongDanAnh() != null && !ls.getDuongDanAnh().isEmpty()) { %>
                            <img src="<%= request.getContextPath() %>/<%= ls.getDuongDanAnh() %>" width="120" class="preview-img"/>
                        <% } else { %>
                            <i>Không có ảnh</i>
                        <% } %>
                    </td>
                </tr>
                <%
                        }
                    } else {
                %>
                <tr>
                    <td colspan="5" class="no-data">Chưa có dữ liệu cỏ nào được ghi nhận cho phiên này</td>
                </tr>
                <%
                    }
                %>
            </tbody>
        </table>
    </div>
</body>
</html>
