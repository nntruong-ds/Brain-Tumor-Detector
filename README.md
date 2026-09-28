# Brain Tumor Detector

Ứng dụng học máy phát hiện khả năng có khối u não từ ảnh MRI. Mô hình CNN (TensorFlow/Keras) phân loại ảnh thành **có u** hoặc **không có u**, kèm dashboard Streamlit để xem phân tích dữ liệu và tải ảnh lên dự đoán.

## Tính năng

- **Quick Project Summary**: tổng quan dự án
- **MRI Visualizer**: ảnh trung bình, độ biến thiên và montage theo nhãn
- **Model Performance**: đường học (accuracy/loss), confusion matrix
- **Brain Tumor Detection**: tải ảnh MRI lên, xem dự đoán và xuất kết quả CSV
- **Project Hypothesis**: giả thuyết và kết luận của dự án

## Công nghệ

Python, NumPy, Pandas, Matplotlib, Seaborn, Plotly, TensorFlow, Keras Tuner, Scikit-learn, Streamlit

## Cấu trúc thư mục

```
├── app.py               # Điểm khởi chạy dashboard
├── app_pages/           # Các trang của dashboard
├── src/                 # Code xử lý và dự đoán
├── jupyter_notebooks/   # Pipeline: dữ liệu, huấn luyện, đánh giá
├── outputs/             # Model và kết quả đánh giá
├── input/validation/    # Ảnh mẫu
└── requirements.txt
```

## Cài đặt và chạy

```bash
git clone https://github.com/TEN_CUA_BAN/brain-tumor-detector.git
cd brain-tumor-detector
pip install -r requirements.txt
streamlit run app.py
```

Ứng dụng chạy tại `http://localhost:8501`.

**Chạy bằng Docker:**

```bash
docker build -t brain-tumor-detector .
docker run -p 8501:8501 brain-tumor-detector
```

## Dữ liệu

Bộ dữ liệu [Brain Tumor trên Kaggle](https://www.kaggle.com/datasets/jakeshbohaju/brain-tumor/data) (ảnh MRI lát cắt ngang, nhãn 1 = có u, 0 = không u).

## Lưu ý

Đây là dự án học tập. Mô hình chưa đạt ngưỡng F1 ≥ 0.95 và recall ≥ 0.98 theo mục tiêu ban đầu, **không dùng để chẩn đoán y tế thực tế**.

## Ghi nguồn

Dự án gốc của [tomdu3](https://github.com/tomdu3/brain-tumor-detector), thuộc chương trình Code Institute.
