import streamlit as st

import streamlit as st

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''

user_input = st.text_input("Enter some text")

if user_input:
    st.session_state['user_input'] = user_input

st.write(f"You entered: {st.session_state['user_input']}")
