import streamlit as st

# Read a value
st.write(st.session_state.key)  # Outputs: value

# Update a value
st.session_state.key = 'value2'  # Attribute API
st.session_state['key'] = 'value2'  # Dictionary-like API
