import streamlit as st
def home_screen():
    st.header('Home Screen')
    col1, col2 = st.columns(2, gap='small')

    with col1:
        if st.button('Teachers Screen', type='primary', key='teachers_screen'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    with col2:
        if st.button('Students Screen', type='primary'):
            st.session_state['login_type'] = 'student'
            st.rerun()

