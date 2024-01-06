import streamlit as st
import numpy as np
import webbrowser
import os

def main():
 if st.sidebar.button("Susisiekti"):
   st.sidebar.markdown("[🎨Visit instagram](https://www.instagram.com/egidijauss/)")
   st.sidebar.markdown("[💖Visit Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")
   st.sidebar.markdown("[🧢Visit Facebook](https://www.facebook.com/EgiFoto)")
   st.sidebar.markdown("")
if __name__ == "__main__":
    main()



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


st.header("Parašyk man žinutę!")

contact_form = """
<form action="https://formsubmit.co/nolessas@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Vardas*" required>
    <input type="text" name="name" placeholder="Telefono numeris*" required>
    <input type="email" name="email" placeholder="El. paštas*" required>
    <input type="text" name="name" placeholder="Šventės data YYYY-MM-DD*" required>
    <textarea name="Žinutė" placeholder="Jūsų pranešimas*" required></textarea>
    <button type="submit">Send</button>
</form>
"""

col1, col2 = st.columns(2)

with col1:
    st.markdown(contact_form, unsafe_allow_html=True)

with col2:
    st.empty()
