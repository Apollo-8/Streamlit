import streamlit as st

# 假设图片文件名为"image.jpg"
image_file = "imgs/1.jpg"

# 创建一个表格
st.write("以下是一个表格，其中包含一个图片：")

# 创建一个表格单元格
row1_col1, row1_col2 = st.columns(2)

# 在第一个单元格中插入图片
with row1_col1:
    st.image(image_file, width=100)

# 在第二个单元格中插入文本
with row1_col2:
    st.write("这是一张图片")

# 创建另一个表格单元格
row2_col1, row2_col2 = st.columns(2)

# 在第一个单元格中插入图片
with row2_col1:
    st.image(image_file, width=100)

# 在第二个单元格中插入文本
with row2_col2:
    st.write("这是另一张图片")
