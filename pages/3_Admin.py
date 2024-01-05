import streamlit as st
import os

# Function to check admin credentials
def authenticate(username, password):
    # Replace with your authentication logic
    return username == "admin" and password == "admin852"

# Function to read messages
def read_messages(user):
    filename = f"{user}_chat.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            messages = file.readlines()
            return messages
    else:
        return []

# Function to send a message
def send_message(user, message):
    filename = f"{user}_chat.txt"
    with open(filename, "a") as file:
        file.write(f"{message}\n")

# Streamlit App
def main():
    st.title("")

    # Default User
    user = "Client"  # You can change this to your desired default name

    # Sidebar Layout
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Login Button
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            # Display the chat box after successful login
            show_chat_box(user)
        else:
            st.error("Invalid credentials. Please try again.")

def show_chat_box(user):
    

    
    

    

    # Display Chat History
    st.title(f"Chat History for {user}")
    messages = read_messages(user)

    # Display entire chat history
    for message in messages:
        st.write(message.strip())

if __name__ == "__main__":
    main()
