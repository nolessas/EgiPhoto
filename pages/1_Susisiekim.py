import streamlit as st
import os

# Function to send a message
def send_message(user, message):
    filename = f"{user}_chat.txt"
    with open(filename, "a") as file:
        file.write(f"{message}\n")

# Streamlit App
def main():
    st.title("Send Message")

    # Default User
    user = "Client"  # You can change this to your desired default name
    
    # User Section
    user_message = st.text_area("Write your message:")
    
    if st.button("Send Message"):
        send_message(user, user_message)
        st.success("Message sent successfully!")

if __name__ == "__main__":
    main()











