import streamlit as st
import numpy as np
import os
from streamlit_lottie import st_lottie
import base64
from natsort import natsorted


# Path to the folder containing images
image_folder = "folder1"

# List all files in the folder and sort them naturally
image_files = natsorted(os.listdir(image_folder))

# Read the watermark image
with open("figures/cigar.jpeg", 'rb') as f:
    watermark_image = f.read()

watermark_bytes = base64.b64encode(watermark_image).decode()
watermark_html = f'<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"><img src="data:image/jpeg;base64,{watermark_bytes}" alt="Watermark" style="width: 100%; height: 100%; object-fit: cover;"></div>'

# Display the watermark
st.markdown(watermark_html, unsafe_allow_html=True)

# Display each image in two columns
col1, col2 = st.columns(2)
for i, image_file in enumerate(image_files):
    # Construct the full path to the image file
    image_path = os.path.join(image_folder, image_file)

    # Display the image in alternating columns
    if i % 2 == 0:
        col1.image(image_path, use_column_width=True, caption=image_file)
    else:
        col2.image(image_path, use_column_width=True, caption=image_file)


image_bytes = base64.b64encode(image).decode()
local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{image_bytes}" alt="Image" width=300></p>'

st.markdown(local_file, unsafe_allow_html=True)


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
