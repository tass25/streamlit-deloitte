import streamlit as st
from utils import get_language_stats, get_most_common_phrases
from style import apply_custom_style

apply_custom_style()
st.title("📊 Analytics Dashboard")

st.markdown('<div class="tts-card">', unsafe_allow_html=True)

st.subheader("🗣️ Most Used Languages")
lang_stats = get_language_stats()
st.bar_chart(lang_stats)

st.subheader("💬 Top 5 Phrases")
phrases = get_most_common_phrases()
if phrases:
    for p, count in phrases:
        st.markdown(f"<div class='message'><b>{p}</b><br><span class='timestamp'>{count} uses</span></div>", unsafe_allow_html=True)
else:
    st.info("No usage data yet.")

st.markdown('</div>', unsafe_allow_html=True)
