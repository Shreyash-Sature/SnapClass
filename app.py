import streamlit as st

def main():
    st.header("This is header")
    name = st.text_input('Enter you name')

    # buttons (side by side)
    # make columns 
    col1, col2 = st.columns(2, gap='small')

    with col1:
        btn1 = st.button('Display name with Hii', type='primary', key='btn1')
        if btn1:
            print("Hiii", name)

    with col2:
        btn2 = st.button('Display name with Bye', type='primary', key='btn2')
        if btn2 :
            print("Bye", name)

    st.markdown("""
            <style>
                     button{
                           background:orange !important; 
                    }
                
                <style>


    """, unsafe_allow_html=True)
main()