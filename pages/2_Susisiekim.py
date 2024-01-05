import streamlit as st

# Function to send a message
def send_message(user, message, phone_number, Filmuoti1, Fotografuoti2, event_date):
    filename = f"{user}_chat.txt"
    with open(filename, "a") as file:
        file.write(f"User: {user}\nMessage: {message}\nPhone Number: {phone_number}\nFilmuoti1 1: {Filmuoti1}\nFotografuoti 2: {Fotografuoti2}\nEvent Date: {event_date}\n\n")

# Streamlit App
def main():
    st.title("Siųsti žinutę!")

    # Default User
    user = "Client"  # You can change this to your desired default name
    
    # User Section
    user_message = st.text_area("Parašykite savo norus:")
    
    # Additional Chatbox for Phone Number
    phone_number = st.text_input("Įveskite savo telefono numerį:")
    
    # Checkmarks
    Filmuoti1 = st.checkbox("Filmuoti")
    Fotografuoti2 = st.checkbox("Fotografuoti")

    # Sidebar Date Input
    event_date = st.date_input("Kada vyksta šventė?", value=None)

    if st.button("Siųsti žinutę"):
        send_message(user, user_message, phone_number, Filmuoti1, Fotografuoti2, event_date)
        st.success("Žinutė išsiųsta sėkmingai!")

if __name__ == "__main__":
    main()
