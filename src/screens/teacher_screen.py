import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard

def teacher_screen():

    
    style_background_dashboard()
    style_base_layout()
    
    #by default open login page at first
    # teacher_screen_login()
    
    #intialize teacher login/register session state
    if 'teacher_login_type' not in st.session_state:
        st.session_state.teacher_login_type = 'login'

    if st.session_state.teacher_login_type =='login':
        teacher_screen_login()
    
    
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()
        


#Teacher login page
def teacher_screen_login():

    #Header Element
    c1, c2 = st.columns(2,vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        back_btn = st.button('Go Back Home',icon=':material/home:', type='secondary', use_container_width=True, key='back_to_home_page')
        if back_btn:
            st.session_state['login_type'] = None
            st.rerun()

    #login page
    st.header('Login using password', text_alignment='center')
    st.space()
    st.space()
    teacher_usr_name = st.text_input("Enter your user id", placeholder='@abhishek.clg')
    teacher_password = st.text_input('Enter your Password', type='password', placeholder='Enter password')
    st.divider()

    col1, col2 = st.columns(2, gap='large')
    with col1:
        #login button
        login_btn = st.button('Login',icon=':material/passkey:', type='secondary',use_container_width=True, key='login_button')
        if login_btn:
            st.markdown(f"""
                <div>
                    <h1>Welcome Back {teacher_usr_name}</h1>
                <div>
        """,unsafe_allow_html=True)
    with col2:
        #register button
        reg_btn = st.button('Register instead',icon=':material/passkey:', type='primary',use_container_width=True, key='register_button')
        if reg_btn:
            st.session_state.teacher_login_type = 'register'
            st.rerun()
            


#Teacher Register Page
def teacher_screen_register():
    #Header Element
    c1, c2 = st.columns(2,vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()

    with c2:
        back_btn = st.button('Go Back Home', type='secondary', key='back_to_home',use_container_width=True)
        if back_btn:
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header('Register your Teacher profile')

    st.space()
    st.space()

    teacher_user_name = st.text_input('Enter your Name', key='teacher_user_name', placeholder='Abhishek Sir')
    teacher_user_id = st.text_input('Enter user id', key='user_id', placeholder='@abhishek.clg' )
    password = st.text_input('Enter Password', type='password', placeholder='Enter password')
    cnf_password = st.text_input('Confirm Password', type='password', placeholder='Confirm password')

    if (password != cnf_password):
        st.markdown("""<p>Password mismatches</p>""",unsafe_allow_html=True)
     
    st.divider()

    c1,c2 = st.columns(2, gap='large')
    with c1:
        reg_btn = st.button('Register now', icon=':material/passkey:', use_container_width=True, type='primary')
    
    with c2:
        login_btn = st.button('Login instead', icon=':material/passkey:', type='secondary', use_container_width=True)
        if login_btn:
            st.session_state.teacher_login_type = 'login'
            st.rerun()




    
