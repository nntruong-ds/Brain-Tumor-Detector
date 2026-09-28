import streamlit as st 
import os 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
from matplotlib.image import imread 
 
import itertools 
import random 
 
 
def page_mri_visualizer_body(): 
    st.write('### Trình trực quan hóa MRI') 
    st.info( 
        '* Khách hàng quan tâm đến việc thực hiện một nghiên cứu để ' 
        'phân biệt trực quan hình ảnh MRI của não khỏe mạnh với hình ảnh ' 
        'MRI của não có khối u.') 
    version = 'v4' 
    if st.checkbox('Hình ảnh trung bình và độ biến thiên'): 
        avg_non_tumor = plt.imread( 
          f'outputs/{version}/avg_var_mri-non-tumor.png') 
        avg_tumor = plt.imread(f'outputs/{version}/avg_var_mri-tumor.png') 
 
        st.warning( 
          '* Chúng tôi nhận thấy các hình ảnh trung bình và độ biến thiên ' 
          'cho thấy một số đặc điểm chung mà chúng ta có thể trực quan ' 
          'phân biệt hình ảnh này với hình ảnh kia. Tuy nhiên, có những ' 
          'trường hợp sự khác biệt này không rõ ràng, nguyên nhân là do ' 
          'sự khác nhau về quá trình phát triển, kích thước và độ tuổi của não. ' 
          'Những yếu tố này khiến việc dự đoán trở nên khá khó khăn.') 
 
        st.image(avg_non_tumor, 
                 caption='MRI não khỏe mạnh - Trung bình và độ biến thiên') 
        st.image(avg_tumor, 
                 caption='MRI não có khối u - Trung bình và độ biến thiên') 
        st.write('---') 
 
    if st.checkbox( 
          'Sự khác biệt giữa hình ảnh MRI não trung bình không có và có khối u'): 
        diff_between_avgs = plt.imread(f'outputs/{version}/avg_diff.png') 
 
        st.warning( 
          '* Chúng tôi nhận thấy nghiên cứu này cho thấy một số đặc điểm ' 
          'chung mà chúng ta có thể trực quan phân biệt hình ảnh này với ' 
          'hình ảnh kia. Nhưng không phải lúc nào cũng như vậy.') 
        st.image(diff_between_avgs, 
                 caption='Sự khác biệt giữa các hình ảnh trung bình') 
 
    if st.checkbox('Bộ ảnh ghép'): 
        st.write('* Để làm mới bộ ảnh ghép, ' 
                 'hãy nhấp vào nút "Tạo bộ ảnh ghép"') 
        my_data_dir = 'input/' 
        labels = os.listdir(os.path.join(my_data_dir, 'validation')) 
        label_to_display = st.selectbox( 
          label='Chọn nhãn', options=labels, index=0) 
    if st.button('Tạo bộ ảnh ghép'): 
        image_montage(dir_path=my_data_dir + '/validation', 
                      label_to_display=label_to_display, 
                      nrows=8, ncols=3, figsize=(10, 25)) 
        st.write('---') 
 
 
def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)): 
    ''' 
    Tạo bộ ảnh ghép của nhãn đã chọn 
    ''' 
 
    sns.set_style('white') 
    labels = os.listdir(dir_path) 
 
    # lấy tập con của lớp mà bạn muốn hiển thị 
    if label_to_display in labels: 
        # kiểm tra xem không gian của bộ ảnh ghép có lớn hơn kích thước tập con không 
        # có bao nhiêu hình ảnh trong thư mục đó 
        images_list = os.listdir(os.path.join(dir_path, label_to_display)) 
        if nrows * ncols < len(images_list): 
            img_idx = random.sample(images_list, nrows * ncols) 
        else: 
            print( 
                f'Giảm nrows hoặc ncols để tạo bộ ảnh ghép. \n' 
                f'Có {len(images_list)} hình ảnh trong tập con. ' 
                f'Bạn đang yêu cầu bộ ảnh ghép với {nrows * ncols} vị trí') 
            return 
 
        # tạo danh sách các chỉ số của trục dựa trên nrows và ncols 
        list_rows = range(0, nrows) 
        list_cols = range(0, ncols) 
        plot_idx = list(itertools.product(list_rows, list_cols)) 
 
        # tạo Figure và hiển thị hình ảnh 
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize) 
        for x in range(0, nrows*ncols): 
            img = imread(os.path.join(dir_path, label_to_display, img_idx[x])) 
            img_shape = img.shape 
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img) 
            axes[plot_idx[x][0], plot_idx[x][1]].set_title( 
              f'Chiều rộng {img_shape[1]}px x Chiều cao {img_shape[0]}px') 
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([]) 
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([]) 
        plt.tight_layout() 
 
        st.pyplot(fig=fig) 
 
    else: 
 
        print('Nhãn bạn chọn không tồn tại.') 
        print(f'Các tùy chọn hiện có là: {labels}') 
