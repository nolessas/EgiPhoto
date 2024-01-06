import streamlit as st
import streamlit as st
import os


def save_to_dataframe(text, df):
    df = df.append({'Text': text}, ignore_index=True)
    return df

def main():
    st.title("Text Input App")

    # Text Input
    user_input = st.text_area("Write something:")

    # Save Button
    if st.button("Save"):
        # Load existing data or create a new DataFrame
        if 'user_input_data.csv' in st.session_state:
            df = st.session_state.user_input_data
        else:
            df = pd.DataFrame(columns=['Text'])

        # Save to DataFrame
        df = save_to_dataframe(user_input, df)
        st.session_state.user_input_data = df

        st.success("Text saved successfully!")

    # Display the saved content
    st.subheader("Saved Content:")
    if 'user_input_data' in st.session_state:
        st.dataframe(st.session_state.user_input_data)

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
