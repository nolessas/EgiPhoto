import streamlit as st
import numpy as np
import webbrowser


def open_instagram():
    youtube_url = 'https://www.instagram.com/egidijauss/'
    webbrowser.open_new_tab(youtube_url)
def main():
    if st.sidebar.button("🎨Instagram"):
        open_instagram()
if __name__ == "__main__":
    main()


def open_youtube():
    youtube_url = 'https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ'
    webbrowser.open_new_tab(youtube_url)
def main():
    if st.sidebar.button("💖Youtube"):
        open_youtube()
if __name__ == "__main__":
    main()


def open_facebook():
    facebook_url = 'https://www.facebook.com/EgiFoto'
    webbrowser.open_new_tab(facebook_url)
def main():
    if st.sidebar.button("🧢Facebook"):
        open_facebook()
if __name__ == "__main__":
    main()

   
   

st.image("logo.png")
st.image("tuscia.png")
st.title(" ")
st.write(" ")

st.image("1.jpg",)
st.image("2.jpg")
st.image("3.jpg")
st.image("4.jpg")
st.image("5.jpg")
st.image("6.jpg")
st.image("7.jpg")
st.image("8.jpg")
st.image("9.jpg")
st.image("10.jpg")
st.image("11.jpg")
st.image("12.jpg")
st.image("13.jpg",)
st.image("14.jpg")
st.image("15.jpg")
st.image("16.jpg")
st.image("17.jpg")
st.image("18.jpg")
st.image("19.jpg")
st.image("20.jpg")
st.image("21.jpg")
st.image("22.jpg")
st.image("23.jpg")
st.image("24.jpg")

st.image('1.jpg', caption='Sunrise by the mountains')



