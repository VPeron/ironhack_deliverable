import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown


setup_page_config()


# content
st.image("static/definition/definition_banner.jpg")
st.title("Definition of Critical Infrastructure")

def_data = render_markdown('static/definition/definition.md')
st.markdown(def_data[:1299], unsafe_allow_html=True)

st.image("static/definition/US_Catogarisation.png")

st.markdown(def_data[1299: 1778], unsafe_allow_html=True)

st.image("static/definition/EU_Categorisation.png")

st.markdown(def_data[1778:2303], unsafe_allow_html=True)

st.image("static/definition/nuclear_stacks.jpg")

st.markdown(def_data[2303:], unsafe_allow_html=True)