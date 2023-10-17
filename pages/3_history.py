import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown
from utils.carrousel import carrousel_build

setup_page_config()

# content
st.title("History of attacks")

st.subheader('Stuxnet')


# image slide
carroussel_paths = [
    'static/history/types_of_powerplants.png',
    'static/history/planttype_hist.png',
    'static/history/powerplants_geodata2019.png',
]

carrousel_build(carroussel_paths, 'hist_demo_path')
st.video('https://www.youtube.com/watch?v=9DCwyuH29SI')

hist_data = render_markdown('static/history/history.md')
st.markdown(hist_data, unsafe_allow_html=True)
