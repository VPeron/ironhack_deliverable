import streamlit as st

from utils.img_bkground import set_background


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

st.title('Guarding Critical Infrastructures: Analyzing and Mitigating Cyber Threats in Nuclear Energy Plants')

# define pages url paths
definition_url = "https://ironhackdeliverable-group5.streamlit.app/definition_of_critical_infrastructure"
risks_and_threats_url = "https://ironhackdeliverable-group5.streamlit.app/risks_and_threats"
history_url = "https://ironhackdeliverable-group5.streamlit.app/history"
attack_vectors_url = "https://ironhackdeliverable-group5.streamlit.app/modern_attack_vectors"
role_of_cyber_url = "https://ironhackdeliverable-group5.streamlit.app/the_role_of_cybersecurity"

st.markdown(f"""
### Group Members:
- Antonio
- Cesar
- Rabia
- Vini  

### Our bootcamp capstone-project aims to illustrate the importance of CyberSecurity in the realms of nuclear energy as critical-infrastruture targets.

---

### INDEX

<a href={definition_url} target="_self"><button style="background-color:GreenYellow;">1. Definition of Critical Infrastructure</button></a>

<a href={risks_and_threats_url} target="_self"><button style="background-color:GreenYellow;">2. Cyber Risks and Threats Relating to Critical Infrastructure</button></a>

<a href={history_url} target="_self"><button style="background-color:GreenYellow;">3. History of Attacks</button></a>

<a href={attack_vectors_url} target="_self"><button style="background-color:GreenYellow;">4. Modern Vectors of Attack</button></a>

<a href={role_of_cyber_url} target="_self"><button style="background-color:GreenYellow;">5. What is The Role of Cybersecurity Within Critical-Infrastructure targets</button></a>
  
""", unsafe_allow_html=True)

# set background img
set_background('static/nuclear_background.png')
