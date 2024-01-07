import streamlit as st
import os
from natsort import natsorted
from PIL import Image
import base64

st.image("logo2.png")


# Function to encode a Matplotlib figure as PNG
def encode_fig(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", pad_inches=0.1)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


# Image workaround
with open("outputs_pdf/foo.png", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    s = my_string.decode('UTF-8')
html = f"""<div style='width:100%; display:block; overflow:hidden'>
                <img style='margin-top:-140px; width:100%' src='data:image/jpeg;base64,{str(s)}'>
           </div>"""
st.markdown(html, unsafe_allow_html=True)

# Matplotlib plot workaround
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
plt.title("Matplotlib Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
st.image(encode_fig(fig), format="PNG", use_container_width=True)

# ... (your other content remains unchanged)

# Define the external CSS
external_css = """
<style>
/* Your custom CSS styles go here */
body {
    background-color: #f0f0f0;
    max-width: 100%;
}

#MainMenu, footer, header {
    display: none;
}
</style>
"""
st.markdown(external_css, unsafe_allow_html=True)

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

# ... (rest of your code remains unchanged)






viewport_meta_tag = """
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
"""
st.markdown(viewport_meta_tag, unsafe_allow_html=True)

# The rest of your Streamlit app remains unchanged
# ...

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")



from PIL import Image

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

        # Display the image
        st.image(img, caption='', use_column_width=True)








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

# Create a layout with three columns
col1, col2, col3 = st.columns(3)

# Content
with col1:
    st.markdown("[🎨Instagram](https://www.instagram.com/egidijauss/)")
with col2:
    st.markdown("[💖Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")
with col3:
    st.markdown("[🧢Facebook](https://www.facebook.com/EgiFoto)")

# Create buttons in each column
if col1.button("Nuotraukos", key="nuotraukos_button", help="Explore photos"):
    display_nuotraukos()  

if col2.button("Vaizdo įrašai", key="vaizdo_irasai_button", help="Watch videos"):
    display_vaizdo_irasai()

if col3.button("Parašyk man žinutę!", key="contact_form_button", help="Write me a message"):
    display_contact_form()
