import streamlit as st
import os

import streamlit as st

import streamlit as st

# Function to check admin credentials
def authenticate(username, password):
    # Replace with your authentication logic
    return username == "admin" and password == "admin123"

# Streamlit App
def main():
    st.title("Admin Login")

    # Sidebar Layout
    st.sidebar.header("Admin Panel")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Login Button
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            # Display the admin panel after successful login
            show_admin_panel()
        else:
            st.error("Invalid credentials. Please try again.")

def show_admin_panel():
    st.title("Admin Panel")
    st.write("Welcome to the admin panel. You can now see the content.")

    # Chatbox functionality
    st.header("Chat Box")
    user_message = st.text_area("Write your message:")
    if st.button("Send Message"):
        send_message(user_message, "User")

    # Display chat history
    for entry in chat:
        st.write(f"{entry['user']}: {entry['message']}")

# Function to send a message
def send_message(message, user):
    chat.append({"user": user, "message": message})

# List to store chat messages
chat = []

if __name__ == "__main__":
    main()




# Function to read messages
def read_messages(user):
    filename = f"{user}_chat.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            messages = file.readlines()
            return messages
    else:
        return []

# Streamlit App
def main():
    st.title("Read Messages")

    # Default User
    user = "Client"  # Make sure it matches the default name in send_message.py

    # Admin Section
    st.title(f"Chat History for {user}")
    messages = read_messages(user)

    # Display entire chat history
    for message in messages:
        st.write(message.strip())

if __name__ == "__main__":
    main()
