import streamlit as st

def apply_custom_style():
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(180deg, #9e92de 0%, #f5f3ff 100%) !important;
            font-family: 'Segoe UI', sans-serif;
            color: black !important;
        }

        h1, h2, h3 {
            color: #4B3FA7 !important;
        }

        label, .stMarkdown, .stTextArea label, .stRadio label, .stCheckbox label {
            color: black !important;
        }

        textarea {
            background-color: #fff !important;
            border: 1.5px solid #b9a7ff !important;
            border-radius: 12px !important;
            font-size: 1rem !important;
            padding: 0.8rem !important;
            color: black !important;
        }

        .stButton > button, .stDownloadButton > button {
            background: linear-gradient(to right, #a78bfa, #7c3aed);
            color: white !important;
            padding: 0.6rem 1.5rem;
            border-radius: 10px;
            font-weight: 600;
            box-shadow: 0 4px 10px rgba(123, 109, 245, 0.3);
            border: none;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            background: linear-gradient(to right, #7c3aed, #a78bfa);
        }

        .tts-card {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(106, 90, 205, 0.1);
            margin: 2rem auto;
            max-width: 800px;
            color: black !important;
        }

        .message {
            background: #f0ecff;
            padding: 1rem;
            margin-bottom: 1rem;
            border-left: 4px solid #8a76e0;
            border-radius: 10px;
            color: black !important;
        }

        .user-msg { border-color: #7b6df5; }
        .bot-msg { border-color: #c2b1fa; }

        .timestamp {
            float: right;
            font-size: 0.75rem;
            color: gray;
        }
    </style>
    """, unsafe_allow_html=True)
