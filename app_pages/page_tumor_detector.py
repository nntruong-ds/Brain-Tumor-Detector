import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities  # noqa
                                                    )


def page_tumor_detector_body():
    st.write('### Phát hiện khối u não')

    st.info(
        '* Khách hàng muốn có khả năng dự đoán sự hiện diện của khối u '
        'trong một hình ảnh MRI não nhất định.'
        )

    st.write(
        '* Việc huấn luyện được thực hiện trên bộ dữ liệu từ Kaggle. Vì vậy, '
        'hình ảnh kiểm tra có thể được lấy từ liên kết này: '
        '[Bộ dữ liệu Kaggle]'
        '(https://www.kaggle.com/datasets/jakeshbohaju/brain-tumor/data).'
        )

    st.write('---')

    images_buffer = st.file_uploader(
        'Tải lên hình ảnh MRI não. Bạn có thể chọn nhiều hơn một hình ảnh.',
        type=['png', 'jpg'], accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f'Mẫu chụp MRI não: **{image.name}**')
            img_array = np.array(img_pil)
            st.image(img_pil,
                     caption=f'Kích thước hình ảnh: {img_array.shape[1]}px chiều rộng x '
                             f'{img_array.shape[0]}px chiều cao')

            version = 'v4'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img,
                                                            version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            new_row = pd.DataFrame([{'Tên': image.name, 'Kết quả': pred_class}])
            df_report = pd.concat([df_report, new_row], ignore_index=True)

        if not df_report.empty:
            st.success('Báo cáo phân tích')
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report),
                        unsafe_allow_html=True)
