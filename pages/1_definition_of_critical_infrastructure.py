import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown


setup_page_config()


# content
st.title("Definition of Critical Infrastructure")

def_data = render_markdown('static/definition.md')
st.markdown(def_data)