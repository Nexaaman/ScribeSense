import streamlit as st
import requests

API_URL = "http://localhost:8000"  # Adjust this if needed

def main():
    st.title("Text Summarization App")

    text_input = st.text_area("Enter text to summarize:", height=200)

    if st.button("Summarize"):
        if text_input:
            # Send the input as a JSON object
            response = requests.post(f"{API_URL}/predict", json={"text": text_input})
            if response.status_code == 200:
                summarized_text = response.json().get("summary")
                st.success("Summarized Text:")
                st.write(summarized_text)
            else:
                st.error("Error occurred while summarizing: " + response.text)
        else:
            st.warning("Please enter some text.")

    if st.button("Train Model"):
        response = requests.get(f"{API_URL}/train")
        if response.status_code == 200:
            st.success("Training started!")
        else:
            st.error("Error occurred while starting training: " + response.text)

if __name__ == "__main__":
    main()
