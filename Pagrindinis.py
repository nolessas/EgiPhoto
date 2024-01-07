import streamlit as st
import os
import io
from natsort import natsorted
from PIL import Image
import base64

st.image("logo2.png")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Embed JavaScript to disable horizontal scrolling for images only
custom_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    function addImageListeners() {
        var images = document.querySelectorAll('img');
        images.forEach(function(img) {
            img.addEventListener('mousedown', function(event) {
                var startX = event.pageX;
                var startY = event.pageY;

                img.addEventListener('mousemove', function(event) {
                    var deltaX = Math.abs(startX - event.pageX);
                    var deltaY = Math.abs(startY - event.pageY);

                    if (deltaX > deltaY) {
                        event.preventDefault();
                    }
                });

                img.addEventListener('mouseup', function() {
                    img.removeEventListener('mousemove', function() {});
                });
            });
        });
    }

    addImageListeners();

    // Add listener to detect when new images are added and apply the script to them
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes) {
                addImageListeners();
            }
        });
    });

    observer.observe(document.body, { childList: true, subtree: true });
});
</script>
"""
st.markdown(custom_js, unsafe_allow_html=True)





viewport_meta_tag = """
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
"""
st.markdown(viewport_meta_tag, unsafe_allow_html=True)


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

col1, col2, col3, col4 = st.columns(4)

import streamlit as st

# Create a layout with 3 rows and 2 columns
col1, col2 = st.columns(2)

# Content in the first row, first column
with col1:
    st.markdown("[🎨Instagram](https://www.instagram.com/egidijauss/)")

# Content in the first row, second column
with col2:
    st.button("Nuotraukos", key="nuotraukos_button", help="Explore photos")

# Content in the second row, first column
with col1:
    st.markdown("[💖Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")

# Content in the second row, second column
with col2:
    st.button("Vaizdo įrašai", key="vaizdo_irasai_button", help="Watch videos")

# Content in the third row, first column
with col1:
    st.markdown("[🧢Facebook](https://www.facebook.com/EgiFoto)")

# Content in the third row, second column
with col2:
    st.button("Parašyk man žinutę!", key="contact_form_button", help="Write me a message")
