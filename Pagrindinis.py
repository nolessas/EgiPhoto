import streamlit as st
import os
import io
from natsort import natsorted
from PIL import Image
import base64
import pandas as pd



# Function to load image with caching
@st.cache_data
def load_image(image_path):
    with open(image_path, "rb") as f:
        return f.read()

# Path to the logo2.png image
image_path = "logo2.png"

# Load the image
image_data = load_image(image_path)

# Encode image data as base64
image_base64 = base64.b64encode(image_data).decode("utf-8")

# HTML, CSS, and JavaScript code for sliding animation
html_code = f"""
<style>
    #logo-container {{
        position: relative;
        width: 100%;
        height: 300px;  /* Adjust the height as needed */
        overflow: hidden;
    }}

    #logo {{
        position: absolute;
        width: 100%;
        height: 100%;
        animation: slide 2s forwards;  /* Adjust the animation duration as needed */
    }}

    @keyframes slide {{
        from {{ left: 100%; }}
        to {{ left: 0; }}
    }}
</style>

<div id="logo-container">
    <img id="logo" src="data:image/png;base64,{image_base64}" alt="Logo">
</div>
"""

# Display the HTML content
st.markdown(html_code, unsafe_allow_html=True)










def display_nuotraukos():
    # Path to the folder containing images
    image_folder = "folder1"

    # List all files in the folder and sort them naturally
    image_files = natsorted(os.listdir(image_folder))

    # Display each image in the folder
    for image_file in image_files:
        # Construct the full path to the image file
        image_path = os.path.join(image_folder, image_file)

        # Open the image using PIL
        img = Image.open(image_path)

        # Calculate the desired width as 50% of the current width
        desired_width = int(img.width * 0.5)

        # Resize the image
        img_resized = img.resize((desired_width, int(img.height * (desired_width / img.width))))

        # Display the resized image
        st.image(img_resized, use_column_width=True)


def display_vaizdo_irasai():
    st.title("Smagaus žiūrėjimo!")

    # Display the video player
    videos = [
        "https://www.youtube.com/watch?v=Tn-KRogA23g",
        "https://www.youtube.com/watch?v=Jt7c8B0bJUE",
        "https://www.youtube.com/watch?v=qoDU7cW7PH4",
        "https://www.youtube.com/watch?v=k2kp3einuKI",
        "https://www.youtube.com/watch?v=_qgFKvRGt_o",
        "https://www.youtube.com/watch?v=jLYcNT3NoBU",
        "https://www.youtube.com/watch?v=rT6dSMf9PuE",
        "https://www.youtube.com/watch?v=QEH55D8sOs8",
        "https://www.youtube.com/watch?v=pq6Zvqp6X7o",
        "https://www.youtube.com/watch?v=74wtkfG9ssw",
    ]

    for video_url in videos:
        st.video(video_url)

def display_contact_form():
    st.header("Parašyk man žinutę!")

    contact_form = """
    <form action="https://formsubmit.co/nolessas@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Vardas*" required>
        <input type="text" name="phone" placeholder="Telefono numeris*" required>
        <input type="email" name="email" placeholder="El. paštas*" required>
        <input type="text" name="event_date" placeholder="Šventės data YYYY-MM-DD*" required>
        <textarea name="message" placeholder="Jūsų pranešimas*" required></textarea>
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px;">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use local CSS for email
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


col1, col2, col3, col4 = st.columns(4)

# Content
#with col1:
    #st.markdown("[🎨Instagram](https://www.instagram.com/egidijauss/)")
#with col2:
    #st.markdown("[💖Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")
#with col3:
    #st.markdown("[🧢Facebook](https://www.facebook.com/EgiFoto)")


if col1.button("Nuotraukos", key="nuotraukos_button", help="Explore photos"):
    display_nuotraukos()  

if col2.button("Vaizdo įrašai", key="vaizdo_irasai_button", help="Watch videos"):
    display_vaizdo_irasai()

if col3.button("Parašyk man žinutę!", key="contact_form_button", help="Write me a message"):
    display_contact_form()



    
def run():
    st.markdown("[Instagram](https://www.instagram.com/egidijauss/)")
    st.markdown("[Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")
    st.markdown("[Facebook](https://www.facebook.com/EgiFoto)")

if st.button("Rask mane internete"):
    # Call the function when the button is pressed
    run()




