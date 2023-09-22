import streamlit as st



def carroussel_build(img_list:list , slide_key:str):
    
    if slide_key not in st.session_state:
        st.session_state[slide_key] = 0

    st.image(img_list[st.session_state[slide_key]])
    slide_button = st.button('next slide')
    if slide_button:
        st.session_state[slide_key] += 1
        if st.session_state[slide_key] >= len(img_list):
            st.session_state[slide_key] = 0