import streamlit as st 


def page_project_hypothesis_body(): 
    st.write('### Giả thuyết và kiểm chứng dự án') 
 
    st.success( 
        "1. Có một niềm tin mạnh mẽ rằng có thể quan sát và nhận thấy sự " 
        "khác biệt về mặt trực quan trong hình ảnh MRI não giữa não khỏe mạnh " 
        "và não có khối u. Do hình ảnh có độ phân giải thấp, việc lọc các hình " 
        "ảnh MRI và so sánh hình ảnh MRI trung bình của não có khối u với hình " 
        "ảnh MRI của não khỏe mạnh sẽ cho thấy sự khác biệt rõ rệt về sắc độ.\n" 
        "2. Mô hình học sâu sử dụng mạng nơ-ron tích chập (CNN) được kỳ vọng " 
        "có thể phân loại chính xác các dữ liệu chưa từng được nhìn thấy của " 
        "hình ảnh MRI não thành hai nhóm: có khối u hoặc không có khối u. " 
        "Các kỹ thuật tăng cường dữ liệu sẽ giúp cải thiện khả năng tổng quát " 
        "hóa của mô hình." 
    ) 
    st.write('---') 
    st.warning( 
        'Tuy nhiên, sau khi kiểm chứng, mô hình ML đã gặp phải một số thách thức:\n\n' 
        '1. **Sự không rõ ràng trong việc phân biệt bằng hình ảnh:** Trong những ' 
        'trường hợp sự khác biệt giữa hình ảnh não khỏe mạnh và não có khối u ' 
        'không rõ rệt, mô hình gặp khó khăn trong việc đưa ra sự phân biệt chính xác.\n\n' 
        '2. **Các chỉ số hiệu suất chưa đạt yêu cầu:** Độ chính xác và điểm F1 ' 
        'của mô hình không đạt được các ngưỡng đã xác định trước, cho thấy mô hình ' 
        'chưa sẵn sàng để được phê duyệt ở trạng thái hiện tại.\n\n' 
        'Do đó, mặc dù dự án cho thấy nhiều tiềm năng, mô hình ML vẫn cần được ' 
        'tinh chỉnh và kiểm thử thêm để đạt được mức độ chính xác mong muốn trong ' 
        'việc phân biệt giữa hình ảnh MRI não khỏe mạnh và não có khối u.' 
    )
