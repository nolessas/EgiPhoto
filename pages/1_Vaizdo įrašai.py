import streamlit as st
import streamlit as st
import os

def save_to_file(text, filename='user_input.txt'):
    with open(filename, 'a') as file:
        file.write(f"{text}\n")

def main():
    st.title("Text Input App")

    # Text Input
    user_input = st.text_area("Write something:")

    # Save Button
    if st.button("Save"):
        save_to_file(user_input)
        st.success("Text saved successfully!")

    # Display the saved content
    st.subheader("Saved Content:")
    if os.path.exists('user_input.txt'):
        with open('user_input.txt', 'r') as file:
            saved_content = file.read()
            st.text(saved_content)

if __name__ == "__main__":
    main()







def main():
    st.title("Smagaus žiūrėjimo!")

    # Display the video player
    st.video("https://www.youtube.com/watch?v=Tn-KRogA23g")
    st.video("https://www.youtube.com/watch?v=Jt7c8B0bJUE")
    st.video("https://www.youtube.com/watch?v=qoDU7cW7PH4")
    st.video("https://www.youtube.com/watch?v=k2kp3einuKI")
    st.video("https://www.youtube.com/watch?v=_qgFKvRGt_o")
    st.video("https://www.youtube.com/watch?v=jLYcNT3NoBU")
    st.video("https://www.youtube.com/watch?v=rT6dSMf9PuE")
    st.video("https://www.youtube.com/watch?v=QEH55D8sOs8")
    st.video("https://www.youtube.com/watch?v=pq6Zvqp6X7o")
    st.video("https://www.youtube.com/watch?v=74wtkfG9ssw")
   



if __name__ == "__main__":
    main()
