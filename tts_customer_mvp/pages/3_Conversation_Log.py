import streamlit as st
from utils import load_history
from style import apply_custom_style

apply_custom_style()
st.title("🧾 Full Conversation Log")

st.markdown('<div class="tts-card">', unsafe_allow_html=True)

history = load_history()

if not history:
    st.info("No conversation history found.")
else:
    for msg in history[::-1]:
        st.markdown(f"""
        <div class="message">
            <span class="timestamp">{msg["time"]} | {msg["lang"]}</span>
            {msg["text"]}
        </div>
        """, unsafe_allow_html=True)

    st.download_button("⬇️ Download Full Log", data=str(history),
                       file_name="conversation_log.txt", mime="text/plain")

st.markdown('</div>', unsafe_allow_html=True)
