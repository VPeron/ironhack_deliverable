import streamlit as st

from utils.img_bkground import set_background
from utils.fetch_markdown import render_markdown


st.set_page_config(
    page_title="Ironhack", 
    page_icon="☢️",
    layout="centered", 
    initial_sidebar_state="collapsed", 
    menu_items=None
    )

set_custom_footer = """
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
st.markdown(set_custom_footer, unsafe_allow_html=True)

# set background img
set_background('static/home/nuclear_background_light.jpg')

# assign pages url paths
definition_url = "https://ironhackdeliverable-group5.streamlit.app/definition_of_critical_infrastructure"
risks_and_threats_url = "https://ironhackdeliverable-group5.streamlit.app/risks_and_threats"
history_url = "https://ironhackdeliverable-group5.streamlit.app/history"
attack_vectors_url = "https://ironhackdeliverable-group5.streamlit.app/modern_attack_vectors"
role_of_cyber_url = "https://ironhackdeliverable-group5.streamlit.app/the_role_of_cybersecurity"
about_us_url = "https://ironhackdeliverable-group5.streamlit.app/about_us"

# content
st.title('Guarding Critical Infrastructures: Analyzing and Mitigating Cyber Threats in Nuclear Energy Plants')

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    
    ### INDEX

    <a href={definition_url} target="_self"><button style="background-color:White;">1. Definition of Critical Infrastructure</button></a>

    <a href={risks_and_threats_url} target="_self"><button style="background-color:White;">2. Cyber Risks and Threats Relating to Critical Infrastructure</button></a>

    <a href={history_url} target="_self"><button style="background-color:White;">3. History of Attacks</button></a>

    <a href={attack_vectors_url} target="_self"><button style="background-color:White;">4. Modern Vectors of Attack</button></a>

    <a href={role_of_cyber_url} target="_self"><button style="background-color:White;">5. What is The Role of Cybersecurity Within Critical-Infrastructure targets</button></a>

    <a href={about_us_url} target="_self"><button style="background-color:White;">6. About Us</button></a>

    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    ### Group Members:
    - **Antonio**
    - **Cesar**
    - **Rabia**
    - **Vini**  
    """, unsafe_allow_html=True)

intro_text = render_markdown('static/home/Introduction.md')
st.markdown(f"""
---
{intro_text}
""", unsafe_allow_html=True)



