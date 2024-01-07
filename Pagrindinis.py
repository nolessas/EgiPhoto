import streamlit as st
import os
import io
from natsort import natsorted
from PIL import Image
import base64
import pandas as pd

st.image("logo2.png")

def display_nuotraukos():
    st.header("Nuotraukos")

    image_folder = "folder1"

    image_files = natsorted(os.listdir(image_folder))

    for image_file in image_files:

        image_path = os.path.join(image_folder, image_file)

        img = Image.open(image_path)

        desired_width = int(img.width * 0.5)

        img_resized = img.resize((desired_width, int(img.height * (desired_width / img.width))))

        st.image(img_resized, use_column_width=True)

def display_vaizdo_irasai():
    st.header("Vaizdo įrašai")  

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

# Function for displaying Pilot data
def display_pilot_data():
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


def display_social_links():

    st.markdown("[Instagram](https://www.instagram.com/egidijauss/)")
    st.markdown("[Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")
    st.markdown("[Facebook](https://www.facebook.com/EgiFoto)")


tabs = {
    "Nuotraukos": display_nuotraukos,
    "Vaizdo įrašai": display_vaizdo_irasai,
    "Parašyk man žinutę": display_pilot_data,
    "Medija": display_social_links,
}

# Display the selected tab
selected_tab = st.selectbox(
    "Choose tab",
    list(tabs.keys())
)
tabs[selected_tab]()
