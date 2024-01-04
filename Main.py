import streamlit as st

from keras.models import load_model

custom_objects = {"YourCustomLayer": YourCustomLayer}
model = load_model('Stock_Predictions_Model.keras', custom_objects=custom_objects)


st.write("Hello **world**!")
