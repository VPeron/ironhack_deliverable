import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown


setup_page_config()


# content
st.title("What is the role of cybersecurity in protecting the nuclear power industry, and how is cybersecurity ensured in nuclear power plants")

cyber_role_data = render_markdown('static/cyber_roles.md')
st.markdown(cyber_role_data)
