import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

# st.write("[![Star](https://img.shields.io/github/stars/Ariba-memon/links.svg?logo=github&style=social)](https://gitHub.com/Ariba-memon/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Ariba Memon, Senior NextJS Developer')

st.info('🚀 Senior NextJS Developer | Generative AI Developer| Modern Full Stack Developer  ')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/@codingtechnicalstar', 'Coding Technical Star YouTube channel', icon_size)

st_button('medium', 'https://medium.com/@aribaabdulqadir', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/aribamemon786', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/thearibamemon/', 'Follow me on LinkedIn', icon_size)

st_button('cup', 'https://www.buymeacoffee.com/aribamemon', 'Buy me a Coffee', icon_size)
