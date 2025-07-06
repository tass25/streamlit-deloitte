import streamlit as st
from style import apply_custom_style

st.set_page_config(page_title="Customer Service Assistant", layout="wide")
apply_custom_style()

st.title("🤖 Customer Service Assistant")

st.markdown('<div class="tts-card">', unsafe_allow_html=True)

st.markdown("""
Welcome to your AI-powered Customer Service MVP

**Use the sidebar** to access:

- 🎤 Text-to-Speech Generator  
- 📊 Analytics Dashboard  
- 🧾 Conversation History  
- ⚙️ Settings (work in progress)
""")

st.markdown('</div>', unsafe_allow_html=True)
