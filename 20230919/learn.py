import streamlit as st
import pandas as pd
from io import BytesIO

st.write("""
# 这是一个简单测试的APP

## This is a simple test app
""")

st.sidebar.header('User Input Parameters')

# 读取图片
# img = open('imgs/1.jpg', 'rb').read()
# img = BytesIO(img)

img = st.image('imgs/1.jpg',width =100)

def user_input_features():
    sepal_width = st.sidebar.slider('Sepal Width', 0.0, 10.0,5.4)
    sepal_height = st.sidebar.slider('Sepal Height', 0.0, 10.0,5.9)
    petal_width = st.sidebar.slider('Petal Width', 0.0, 10.0,1.0)
    petal_height = st.sidebar.slider('Petal Height', 0.0, 10.0,1.8)

    data = {
        'sepal_width': sepal_width,
        'sepal_height': sepal_height,
        'petal_width': petal_width,
        'petal_height': petal_height  }
    features = pd.DataFrame(data, index=[0])
    return features

features = user_input_features()
st.subheader('User Input Parameters')
st.write(features)

