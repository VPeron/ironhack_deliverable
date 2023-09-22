import streamlit as st

def setup_page_config():
    st.set_page_config(
        page_title="Ironhack", 
        page_icon="☢️",
        layout="centered", 
        initial_sidebar_state="collapsed", 
        menu_items=None
        )

    insert_footer = """
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
    st.markdown(insert_footer, unsafe_allow_html=True)

    # home button
    home_url = "https://ironhackdeliverable-group5.streamlit.app/"
    st.markdown(f"""
    <a href={home_url} target="_self"><button style="background-color:GreenYellow;">Home</button></a>
    """, unsafe_allow_html=True)