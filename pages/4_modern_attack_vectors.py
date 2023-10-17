import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown


setup_page_config()


# content
st.title("Modern Vectors of Attack")

threat_data = render_markdown('static/modern_attacks.md')

st.markdown(threat_data, unsafe_allow_html=True)