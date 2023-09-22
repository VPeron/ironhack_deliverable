import streamlit as st

st.set_page_config(page_title="Ironhack", page_icon="☢️",layout='wide')

hide_streamlit_style = """
    <style>
    
    footer {
        visibility:hidden;
    }
    footer:after {
        content: 'Ironhack deliverable - Group 5 ®️';
        visibility: visible;
        display: block;
        position: relative;
        #background-color: red;
        padding: 5px;
        top: 2px;
    }
    </style>
"""
# Inject CSS with Markdown
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title('Critical Infrastructures: Analyzing and Mitigating Cyber Threats in Nuclear Energy Plants (?)')

st.image('https://www.worldatlas.com/r/w1200-q80/upload/3d/93/c7/shutterstock-1574089963.jpg')

