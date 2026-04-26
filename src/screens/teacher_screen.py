import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout

def teacher_screen():

    style_background_dashboard()
    style_base_layout()
    st.header('Teacher Screen')


    back_btn = st.button('Home Screen',type='primary')
    if back_btn :
        st.session_state['login_type'] = None
        st.rerun()
