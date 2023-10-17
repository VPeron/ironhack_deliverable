import streamlit as st

from utils.load_boilerplate import setup_page_config

setup_page_config()

st.title("About Us")

st.markdown("""
            
---
   
# Antonio

---

# Cesar

---

# Rabia

---

# Vini

---
 
            """, unsafe_allow_html=True)

st.image("static/about/ironhack_logo.png")