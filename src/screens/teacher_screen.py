import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.footer import footer_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()

    

def teacher_screen_login():
    col1,col2=st.columns(2,vertical_alignment='center',gap='xxlarge')

    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home", type="secondary", key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()
        

    st.header("Login using password",text_alignment='center')

    st.space()
    st.space()
    teacher_username=st.text_input("Enter Username",placeholder='ananyaroy')

    teacher_pass=st.text_input("Enter Password",type="password",placeholder="Enter password")

    st.divider()

    btnc1,btnc2=st.columns(2)

    with btnc1:
        st.button("Login",icon=":material/passkey:",shortcut="control+enter",width="stretch")

    with btnc2:
        if st.button("Register Instead",icon=":material/passkey:",type="primary",width="stretch"):
            st.session_state.teacher_login_type="register"

    footer_dashboard()




def teacher_screen_register():
    col1,col2=st.columns(2,vertical_alignment='center',gap='xxlarge')

    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home", type="secondary", key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()

    st.header("Register Your Teacher Profile")

    st.space()
    st.space()

    teacher_username=st.text_input("Enter Username",placeholder='ananyaroy')

    teacher_name=st.text_input("Enter Name",placeholder='Ananya Roy')

    teacher_pass=st.text_input("Enter Password",type="password",placeholder="Enter password")

    confirm_pass=st.text_input("Confirm Password",type="password",placeholder="Enter password")

    st.divider()

    btnc1,btnc2=st.columns(2)

    with btnc1:
        st.button("Register Now",icon=":material/passkey:",shortcut="control+enter",width="stretch")

    with btnc2:
        if st.button("Login Instead",icon=":material/passkey:",type="primary",width="stretch"):
            st.session_state.teacher_login_type="login"

    footer_dashboard()