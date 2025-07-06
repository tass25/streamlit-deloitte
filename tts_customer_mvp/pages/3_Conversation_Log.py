import streamlit as st
from utils import load_history

st.title("🧾 Conversation Log")

history = load_history()

if not history:
    st.info("No history available.")
else:
    for msg in history[::-1]:
        role = "🧑 User" if msg["role"] == "user" else "🤖 Assistant"
        st.markdown(f"""
        **{role}** at *{msg["time"]}* ({msg["lang"]}):  
        > {msg["text"]}
        """)
    st.download_button("⬇️ Download Full Log", data=str(history),
                       file_name="conversation_log.txt", mime="text/plain")
