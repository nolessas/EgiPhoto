import streamlit as st
import streamlit as st
import os
import pandas as pd

def main():
    st.title("User Input Text Saver")

    # Get user input
    user_input = st.text_input("Enter your text:")

    if st.button("Save Text"):
        # Load existing data or create a new DataFrame
        try:
            df = pd.read_csv("user_input.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Text"])

        # Append the new user input to the DataFrame
        df = df.append({"Text": user_input}, ignore_index=True)

        # Save the DataFrame to a CSV file
        df.to_csv("user_input.csv", index=False)

        st.success("Text saved successfully!")

    # Display the existing data
    st.title("Existing User Input")
    try:
        existing_data = pd.read_csv("user_input.csv")
        st.dataframe(existing_data)
    except FileNotFoundError:
        st.info("No existing data.")

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
