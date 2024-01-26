
import streamlit as st
import os
from natsort import natsorted
from PIL import Image

st.image("logo2.png")

def display_nuotraukos():
    image_folder = "folder1"
    image_files = natsorted(os.listdir(image_folder))
    max_width = st.sidebar.slider('Max image width', 100, 600, 300)  # Slider to adjust image width

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        desired_width = min(int(img.width * 0.5), max_width)  # Set the desired width as the smaller of half the original width or max_width
        img_resized = img.resize((desired_width, int(img.height * (desired_width / img.width))))
        st.image(img_resized)


# CSS to hide the fullscreen button
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

# Call this before displaying images
st.markdown(hide_img_fs, unsafe_allow_html=True)

def display_vaizdo_irasai():
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

def display_pilot_data():
    contact_form = """
    <form action="https://formsubmit.co/nolessas@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Vardas*" required>
        <input type="text" name="phone" placeholder="Telefono numeris*" required>
        <input type="email" name="email" placeholder="El. paštas*" required>
        <input type="text" name="event_date" placeholder="Šventės data YYYY-MM-DD*" required>
        <textarea name="message" placeholder="Jūsų pranešimas*" required></textarea>
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px;">Siūsti!</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

         # Use local CSS for email
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

def display_social_links():
    st.markdown("<p align='center'><a href='https://www.instagram.com/egidijauss/'>🎨Instagram</a></p>", unsafe_allow_html=True)
    st.markdown("<p align='center'><a href='https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ'>🚩Youtube</a></p>", unsafe_allow_html=True)
    st.markdown("<p align='center'><a href='https://www.facebook.com/EgiFoto'>🌊Facebook</a></p>", unsafe_allow_html=True)





st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
choose_main = st.radio("", ("Nuotraukos", "Vaizdo įrašai", "Parašyk man žinutę!", "Media"))

if choose_main == "Nuotraukos":
    st.title("Nuotraukos")
    display_nuotraukos()
if choose_main == "Vaizdo įrašai":
    st.title("Vaizdo įrašai")
    display_vaizdo_irasai()
if choose_main == "Parašyk man žinutę!":
    st.title("Parašyk man žinutę!")
    display_pilot_data()
if choose_main == "Media":
    st.title("Media")
    display_social_links()
