import streamlit as st
from PIL import Image

import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)







st.header("EgiPhoto", divider="rainbow")
st.subheader("Welcome to my webpage")

st.markdown('''
    
            
    - Item one
    - Item two
    - Item three
            

    


st.image(example_img)
