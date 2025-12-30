import streamlit as st
from PIL import Image

st.title('タイトル2')
st.caption("これはテスト用アプリです")

image = Image.open('./data/miku.png')
st.image(image, width=400)