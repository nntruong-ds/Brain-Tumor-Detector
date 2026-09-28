import streamlit as st 


def page_summary_body(): 

    st.write('### Tóm tắt nhanh về dự án của Trường siêu đẹp sai') 

    st.info( 
        'Brain Tumor Detector là một dự án về khoa học dữ liệu và học máy. ' 
        'Mục tiêu kinh doanh của dự án này là phân biệt não khỏe mạnh và não ' 
        'có khối u dựa trên hình ảnh chụp MRI não. Dự án được thực hiện bằng ' 
        'Dashboard Streamlit và cho phép khách hàng tải lên hình ảnh MRI não ' 
        'để dự đoán khả năng có khối u. Dashboard cung cấp kết quả phân tích ' 
        'dữ liệu, mô tả và phân tích các giả thuyết của dự án, cũng như thông tin ' 
        'chi tiết về hiệu suất của mô hình học máy. ' 
        ) 

    

    st.success( 
        'Dự án có 2 yêu cầu kinh doanh:\n' 
        '* 1 - Khách hàng muốn có một nghiên cứu về bộ dữ liệu đã thu thập\n' 
        '* 2 - Khách hàng muốn phát triển một mô hình ML để có thể xác định ' 
        'khối u não từ hình ảnh chụp MRI.' 
        )
