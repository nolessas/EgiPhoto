import streamlit as st
import numpy as np
import os
from streamlit_lottie import st_lottie
import base64
from natsort import natsorted

st.title("")

# Use columns to create a responsive layout
col1, col2 = st.columns(2)
col1.write("Left column content")
col2.write("Right column content")

st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        body {
            margin: 0;
            padding: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)




st.image("logo2.png")
    
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

# List all files in the folder and sort them naturally
image_files = natsorted(os.listdir(image_folder))

# Display each image in the folder
for image_file in image_files:
    # Construct the full path to the image file
    image_path = os.path.join(image_folder, image_file)

    # Display the image
    st.image(image_path, use_column_width=True)

# Read and display a specific image
with open("figures/cigar.jpeg", 'rb') as f:
    image = f.read()

image_bytes = base64.b64encode(image).decode()
local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{image_bytes}" alt="Image" width=300></p>'

st.markdown(local_file, unsafe_allow_html=True)
