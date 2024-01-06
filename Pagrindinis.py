import streamlit as st
import numpy as np
import datetime
import webbrowser
import os
from streamlit_lottie import st_lottie
from PIL import Image
import requests
import json

st.image("logo2.png")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

def load_lottiefile(filepath: str):
   with open(filepath, "r") as f:
      return json.load(f)

lottie_coding = load_lottiefile("lottiefile/coding.json")

st.title("")
st_lottie(
   lottie_coding,
   speed=1,
   reverse=True,
   loop=True,
)



    
def main():
 if st.sidebar.button("Susisiekti"):
   st.sidebar.markdown("[🎨Visit instagram](https://www.instagram.com/egidijauss/)")
   st.sidebar.markdown("[💖Visit Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")
   st.sidebar.markdown("[🧢Visit Facebook](https://www.facebook.com/EgiFoto)")
   st.sidebar.markdown("")
if __name__ == "__main__":
    main()




# Path to the folder containing images
image_folder = "folder1"

# List all files in the folder
image_files = os.listdir(image_folder)

# Display each image in the folder
for image_file in image_files:
    # Construct the full path to the image file
    image_path = os.path.join(image_folder, image_file)

    # Display the image
    st.image(image_path, use_column_width=True)



