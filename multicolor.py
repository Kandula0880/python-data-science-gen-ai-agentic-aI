import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# set streamlit page config
st.set_page_config(page_title="Elephant Image Processor",layout="wide")

# Tittle
st.title("Elephant Image - Multi-Color Channel Visualizer")

# Load image from url
@st.cache_data
def load_image():
    url = "https://thumbs.dreamstime.com/b/elephant-25928218.jpg"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

#Load and dispaly Image
elephant = load_image()
st.image(elephant,caption="Original Elephant Image",use_container_width=True)

# Convert to Numpy array
elephant_np = np.array(elephant)
R, G, B = elephant_np[:,:,0],elephant_np[:,:,1],elephant_np[:,:,2]

# create chaneel images
red_img = np.zeros_like(elephant_np)
green_img = np.zeros_like(elephant_np) 
blue_img = np.zeros_like(elephant_np)

red_img[:,:,0] = R
green_img[:,:,1] = G
blue_img[:,:,2] = B

# Display RGB channels
st.subheader("RGB channel visualization")
col1,col2,col3 = st.columns(3)

with col1:
    st.image(red_img,caption="Red Channel",use_container_width=True)

with col2:
    st.image(green_img,caption="Green Channel",use_container_width=True)

with col3:
    st.image(blue_img,caption="Blue Channel",use_container_width=True)

# Gray + colormap
st.subheader("Colormaped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis","plasma","inferno","magma","cividis","hot","cool","gray"]
)

elephant_gray = elephant.convert("L")
elephant_gray_np = np.array(elephant_gray)

# plot using matplotlib with colormap
fig,ax = plt.subplots(figsize=(6,4))
im = ax.imshow(elephant_gray_np,cmap=colormap)
plt.axis("off")

# Do not use : plt.show()
# Use this instead
st.pyplot(fig)