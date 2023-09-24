import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown
from utils.carrousel import carrousel_build

setup_page_config()

# content
st.title("History of attacks")

# image slide
carroussel_paths = [
    'static/types_of_powerplants.png',
    'static/planttype_hist.png',
    'static/powerplants_geodata2019.png',
]

carrousel_build(carroussel_paths, 'hist_demo_path')

hist_data = render_markdown('static/history.md')
st.markdown(hist_data)
