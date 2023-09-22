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

definition_url = "https://ironhackdeliverable-group5.streamlit.app/definition_of_critical_infrastructure"

st.markdown(f"""
### Group Members:
- Antonio
- Cesar
- Rabia
- Vini  

*Our end-of-bootcamp project aims to illustrate the importance of CyberSecurity in the realms of 
nuclear energy and critical-infrastruture.*

### INDEX

<a href={definition_url}><button style="background-color:GreenYellow;">1. Definition of Critical Infrastructure</button></a>
1. Definition of Critical Infrastructure
2. Cyber Risks and Threats Relating to Critical Infrastructure

    2.1. A comprehensive analysis of the threat landscape 
    
    2.2. Motivations behind cyber-attacks on critical infrastructure (espionage etc.)
    
    2.3. An assessment of vulnerabilities and potential impacts associated with the attacks
    
    2.4. Implications of Cyber-Attacks on Nuclear Infrastructure (-Safety and Radiation Risk  -Political and Geopolitical Consequences)
    
3. History of how it's been attacked in the past (Dtrack, Conficker, Operation Sharpshooter, Stuxnet)
4. Modern Vectors of Attack
5. What is the role of cybersecurity in protecting the nuclear power industry, and how is cybersecurity ensured in nuclear power plants?
  
            """, unsafe_allow_html=True)

# st.button('[1. Definition of Critical Infrastructure](https://ironhackdeliverable-group5.streamlit.app/definition_of_critical_infrastructure)', key='definition')
# st.button('[2. Cyber Risks and Threats Relating to Critical Infrastructure](https://ironhackdeliverable-group5.streamlit.app/risks_and_threats)', key='risks and threats')
# st.button("[3. History of how it's been attacked in the past](https://ironhackdeliverable-group5.streamlit.app/history)", key='history')
# st.button("[4. Modern Vectors of Attack](https://ironhackdeliverable-group5.streamlit.app/modern_attack_vectors)", key='modern attacks')
# st.button("[5. the role of cybersecurity](https://ironhackdeliverable-group5.streamlit.app/the_role_of_cybersecurity)", key='role of cyber')



