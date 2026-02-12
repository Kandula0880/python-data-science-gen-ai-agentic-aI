# Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np

# Add a title and Description
st.title("My first streamlit app")
st.write("This is a simple app to demonstrate the baic functionalities of streamlit.")

# Interactive widgets in  the sidebar
st.sidebar.header("User Input Features")

# Text Input
user_name = st.sidebar.text_input("What is your name?","Kasi Reddy")

# slider
age = st.sidebar.slider("Select your age",0 ,100,25)

# select box
favoriate_color = st.sidebar.selectbox("What is your favoriate color?",["Blue","Red","Green","Yellow"])

# Main page content
st.header(f"Welcome, {user_name}!")
st.write(f"You age {age} years old and your favoriate color is {favoriate_color}.")

# Displaying Data
st.subheader("Here's some random data:")

# create a sample data frame
data = pd.DataFrame(
    np.random.randn(10,5),
    columns = ("col %d"  % i for i in range(5))
)
st.dataframe(data)

#checkbox to show/hide content
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# Button to trigger an action
if st.button("Say Hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")