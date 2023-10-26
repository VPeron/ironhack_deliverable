import streamlit as st

from utils.load_boilerplate import setup_page_config

setup_page_config()

st.title("About Us")

st.image("static/about/ironhack_logo.png")

st.markdown("""
   
# Antonio

---

# César

---

# Rabia

---

# Vinicius Peron

[Linkedin](https://www.linkedin.com/in/vinicius-p-9a9197270)

[Github](https://github.com/VPeron)

[TryHackMe](https://tryhackme.com/p/Crackpot)

---
 
""", unsafe_allow_html=True)

