import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown


setup_page_config()


# content
st.title("Cyber Risks and Theats Related to Critical Infrastructure")

threat_data = render_markdown('static/threats.md')
st.markdown(threat_data)