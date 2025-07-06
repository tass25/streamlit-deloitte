import streamlit as st
from gtts import gTTS
import tempfile
from utils import add_to_history
from style import apply_custom_style

apply_custom_style()
st.title("🎤 Text-to-Speech Generator")

def generate_gtts_audio(text, lang, slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown('<div class="tts-card">', unsafe_allow_html=True)

language = st.radio("🌐 Choose Language:", ("English", "Arabic", "French"))
slow_speed = st.toggle("🐢 Slow Speech", value=False)

# Language setup
if language == "English":
    lang_code = 'en'
    examples = [
        "Thank you for contacting customer support.",
        "We apologize for the inconvenience caused.",
        "Please provide your account number.",
        "Can you confirm your email address?",
        "We are processing your request."
    ]
elif language == "Arabic":
    lang_code = 'ar'
    examples = [
        "شكرًا لتواصلك مع دعم العملاء.",
        "نعتذر عن الإزعاج.",
        "من فضلك قدم رقم حسابك.",
        "هل يمكنك تأكيد بريدك الإلكتروني؟",
        "نقوم بمعالجة طلبك حاليًا."
    ]
else:
    lang_code = 'fr'
    examples = [
        "Merci de contacter le support client.",
        "Nous nous excusons pour les désagréments.",
        "Veuillez fournir votre numéro de compte.",
        "Pouvez-vous confirmer votre adresse e-mail?",
        "Votre demande est en cours de traitement."
    ]

with st.expander("💬 Try Example Sentences"):
    for ex in examples:
        if st.button(f"▶️ {ex}"):
            audio_path = generate_gtts_audio(ex, lang_code, slow_speed)
            st.audio(audio_path, format="audio/mp3")
            add_to_history("bot", ex, lang_code)

user_input = st.text_area("✍️ Enter your own message:")

if st.button("🔊 Generate Speech"):
    if user_input.strip():
        audio_path = generate_gtts_audio(user_input, lang_code, slow_speed)
        st.audio(audio_path, format="audio/mp3")
        st.download_button("⬇️ Download Audio", data=open(audio_path, "rb"), file_name="output.mp3", mime="audio/mp3")
        add_to_history("user", user_input, lang_code)
        st.session_state.history.append({"role": "user", "text": user_input})
    else:
        st.warning("⚠️ Please enter some text.")

if st.button("🗑️ Clear Session History"):
    st.session_state.history.clear()

if st.session_state.history:
    st.subheader("🕓 Conversation History (This Session)")
    for msg in st.session_state.history[::-1]:
        role_class = "user-msg" if msg["role"] == "user" else "bot-msg"
        st.markdown(f"""
        <div class="message {role_class}">
            <span class="timestamp">Now</span>
            {msg["text"]}
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
