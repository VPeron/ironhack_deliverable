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

st.markdown("""
### Group Members:
- Antonio
- Cesar
- Rabia
- Vini  

*Our end-of-bootcamp project aims to illustrate the importance of CyberSecurity in the realms of 
nuclear energy and critical-infrastruture.*

### INDEX

1. Definition of Critical Infrastructure
2. Cyber Risks and Threats Relating to Critical Infrastructure

    2.1. A comprehensive analysis of the threat landscape 
    
    2.2. Motivations behind cyber-attacks on critical infrastructure (espionage etc.)
    
    2.3. An assessment of vulnerabilities and potential impacts associated with the attacks
    
    2.4. Implications of Cyber-Attacks on Nuclear Infrastructure (-Safety and Radiation Risk  -Political and Geopolitical Consequences)
    
3. History of how it's been attacked in the past (Dtrack, Conficker, Operation Sharpshooter, Stuxnet)
4. Modern Vectors of Attack
5. What is the role of cybersecurity in protecting the nuclear power industry, and how is cybersecurity ensured in nuclear power plants?
  
            """)



