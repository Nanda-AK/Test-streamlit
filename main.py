import streamlit as st

# Initialize session state variables
if 'input_text' not in st.session_state:
    st.session_state.input_text = ''
if 'results' not in st.session_state:
    st.session_state.results = []

# Function to process input and update results
def process_input():
    st.session_state.results.append(st.session_state.input_text)
    st.session_state.input_text = ''  # Reset the input field

# Input text box
st.text_input("Enter some text", key='input_text')

# Button to process input
st.button("Submit", on_click=process_input)

# Display results
st.write("Results:")
for result in st.session_state.results:
    st.write(result)

