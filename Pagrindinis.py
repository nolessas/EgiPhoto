import streamlit as st
import numpy as np
import os
from streamlit_lottie import st_lottie
import base64
from natsort import natsorted

# Viewport Meta Tag to prevent wiggling on iPhone
st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """,
    unsafe_allow_html=True,
)

# Path to the folder containing images
image_folder = "folder1"

# List all files in the folder and sort them naturally
image_files = natsorted(os.listdir(image_folder))

# Use columns to create a responsive layout
col1, col2 = st.columns(2)

# Display each image in two columns
for i, image_file in enumerate(image_files):
    # Construct the full path to the image file
    image_path = os.path.join(image_folder, image_file)

    # Display the image in alternating columns
    if i % 2 == 0:
        col1.image(image_path, use_column_width=True, caption=f"Image {i+1}")
    else:
        col2.image(image_path, use_column_width=True, caption=f"Image {i+1}")



    
def main():
 if st.sidebar.button("Susisiekti"):
   st.sidebar.markdown("[🎨Visit instagram](https://www.instagram.com/egidijauss/)")
   st.sidebar.markdown("[💖Visit Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")
   st.sidebar.markdown("[🧢Visit Facebook](https://www.facebook.com/EgiFoto)")
   st.sidebar.markdown("")
if __name__ == "__main__":
    main()



