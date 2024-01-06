import streamlit as st
import streamlit as st
import os
import pandas as pd


import streamlit as st
import pandas as pd

def main():
    st.title("User Input Text Saver")

    # Get user input
    user_input = st.text_input("Enter your text:")

    if st.button("Save Text"):
        try:
            # Try loading existing data
            df = pd.read_csv("user_input.csv")
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame
            df = pd.DataFrame(columns=["Text"])

        # Append the new user input to the DataFrame
        try:
            df = df.append({"Text": user_input}, ignore_index=True)
        except Exception as e:
            st.error(f"Error appending to DataFrame: {e}")
            return

        # Save the DataFrame to a CSV file
        try:
            df.to_csv("user_input.csv", index=False)
            st.success("Text saved successfully!")
        except Exception as e:
            st.error(f"Error saving DataFrame to CSV: {e}")
            st.error(f"DataFrame content:\n{df}")

    # Display the existing data
    st.title("Existing User Input")
    try:
        existing_data = pd.read_csv("user_input.csv")
        st.dataframe(existing_data)
    except FileNotFoundError:
        st.info("No existing data.")
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")

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
