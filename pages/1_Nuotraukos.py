import streamlit as st
import numpy as np
import os
from streamlit_lottie import st_lottie
import json
from natsort import natsorted
  
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


