import streamlit as st
from PIL import Image

st.title('apprication')
st.caption('test')

image = Image.open('./data/miku.png')
st.image(image, width=400)