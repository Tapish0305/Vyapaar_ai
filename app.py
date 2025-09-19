import streamlit as st
import requests
import os

# Get Langflow API Key from environment variable
API_KEY = "sk-LxGC_1gQxpsV-h2zZkI7XwH9VQxAx6Nc9Tk_zDXtQWc"
if not API_KEY:
    st.error("Error: LANGFLOW_API_KEY environment variable is not set.")
    st.stop()

# Langflow API endpoint URL (update host/port as per your server)
LANGFLOW_URL = "http://localhost:7860/api/v1/run/f19bea7d-0cfc-432e-8629-2883d21ccab5"

def run_langflow(input_text):
    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": input_text
    }
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    try:
        response = requests.post(LANGFLOW_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Streamlit UI
st.title("Langflow + Streamlit AI App")

user_input = st.text_input("Enter your message:")

if st.button("Run Flow"):
    if user_input.strip() == "":
        st.warning("Please enter some input text.")
    else:
        with st.spinner("Running flow..."):
            result = run_langflow(user_input)
            if "error" in result:
                st.error(f"API request error: {result['error']}")
            else:
                st.success("Flow output:")
                st.json(result)
