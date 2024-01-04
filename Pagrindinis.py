import streamlit as st
import numpy as np
import datetime



st.title("EgiPhoto")
st.write("")

st.image('1.jpg', caption='Sunrise by the mountains')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("")
   st.image("4.jpg")

with col2:
   st.header("")
   st.image("5.jpg")

with col3:
   st.header("")
   st.image("6.jpg")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("")
   st.image("7.jpg")

with col2:
   st.header("")
   st.image("8.jpg")

with col3:
   st.header("")
   st.image("9.jpg")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("")
   st.image("10.jpg")

with col2:
   st.header("")
   st.image("11.jpg")

with col3:
   st.header("")
   st.image("12.jpg")


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Pasirinkite dominančią tema",
    ("Filmavimas", "Fotografavimas", "Abu")
)
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Iš klaipėdos raj.?",
        ("Taip", "Ne")
    )

st.sidebar.text_area("Pasidalinkite smulkmenomis!:")


d = st.sidebar.date_input("Kada vyksta šventė?", value=None)

if st.sidebar.button('Užsakom!', key='uzsakom_button', type="primary"):
    st.sidebar.write('Ačiū, greit susisieksim!')
