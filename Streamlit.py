# 1.Import Streamlit
import streamlit as st

# 2. Add  a title to your first app
st.title("My first streamlit app created by kandula chinna kasi reddy")

# 3.Add some text
st.write("Welcome! This app calculates the square of a number.")

# 4.create an interactive slider
st.header("Select a Number")
number = st.slider("Pick a number",0,100,25) # min,max,bydefault

# 5. calculate and display the result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")

