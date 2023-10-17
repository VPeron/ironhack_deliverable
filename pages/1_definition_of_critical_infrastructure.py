import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown


setup_page_config()


# content
st.image("static/definition_banner.jpg")
st.title("Definition of Critical Infrastructure")

def_data = render_markdown('static/definition.md')
st.markdown(def_data, unsafe_allow_html=True)