import streamlit as st
import requests

API_URL = "http://localhost:8000"
def main():
    st.title("ScribeSense")
    st.text("A text Summarization Application :)")

    col1, col2 = st.columns([1, 3])
    with col1:
        length_penalty = st.slider("summary context", min_value=0.0, max_value=2.0, value=1.0, step=0.1)


    text_input = st.text_area("Enter text to summarize:", height=200)
    if st.button("Summarize"):
        if text_input:
            response = requests.post(f"{API_URL}/predict", json={"text": text_input, "length_penalty":length_penalty})
            if response.status_code == 200:
                summarized_text = response.json().get("summary")
                st.success("Summarized Text:")
                st.write(summarized_text)
            else:
                st.error("Error occurred while summarizing: " + response.text)
        else:
            st.warning("Please enter some text.")

    st.text("Created by Aman")

if __name__ == "__main__":
    main()
