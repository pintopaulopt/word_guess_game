import streamlit as st

# Title of the app
st.title('My First Streamlit App')

# Display a text
st.write("Hello, world!")

# Create a slider
number = st.slider('Pick a number', 0, 100)
st.write(f'You picked: {number}')

# Create a simple text input
name = st.text_input('Enter your name')
st.write(f'Hello, {name}!')
