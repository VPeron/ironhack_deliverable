import streamlit as st


st.set_page_config(
    page_title="Ironhack", 
    page_icon="☢️",
    layout="wide", 
    initial_sidebar_state="collapsed", 
    menu_items=None
    )

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


st.title("Cyber Risks and Threats Relating to Critical Infrastructure")



st.markdown("""
            
    2.1. A comprehensive analysis of the threat landscape 
    
    2.2. Motivations behind cyber-attacks on critical infrastructure (espionage etc.)
    
    2.3. An assessment of vulnerabilities and potential impacts associated with the attacks
    
    2.4. Implications of Cyber-Attacks on Nuclear Infrastructure (-Safety and Radiation Risk  -Political and Geopolitical Consequences)

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.    
            
            """)