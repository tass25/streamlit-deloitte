import streamlit as st
from style import apply_custom_style

apply_custom_style()
st.title("⚙️ Settings")

st.markdown('<div class="tts-card">', unsafe_allow_html=True)

st.info("This section will support:")
st.markdown("""
- Default language and speed preferences  
- Theme mode (light/dark)  
- Voice choice (future option)  
- Export/import user settings
""")

st.markdown('</div>', unsafe_allow_html=True)
