import streamlit as st
from utils import get_language_stats, get_most_common_phrases

st.title("📊 Analytics Dashboard")

st.subheader("🗣️ Most Used Languages")
lang_stats = get_language_stats()
st.bar_chart(lang_stats)

st.subheader("💬 Most Common Phrases")
top_phrases = get_most_common_phrases()

for phrase, count in top_phrases:
    st.write(f"🔹 **{phrase}** — used `{count}` times")
