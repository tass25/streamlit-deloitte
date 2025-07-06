import streamlit as st
from gtts import gTTS
import tempfile
from utils import add_to_history

def generate_gtts_audio(text, lang, slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

st.title("🎤 Text-to-Speech Generator")

# Initialize session history
if "history" not in st.session_state:
    st.session_state.history = []

# Language & Speed
language = st.radio("🌐 Choose language:", ("English", "Arabic", "French"))
slow = st.toggle("🐢 Slow Speech", value=False)

# Language logic
if language == "English":
    lang_code = 'en'
    examples = [
        "Thank you for contacting customer support. How can we assist you today?",
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

# Show examples
with st.expander("💬 Try Example Sentences"):
    for ex in examples:
        if st.button(f"▶️ {ex}"):
            audio_path = generate_gtts_audio(ex, lang_code, slow)
            st.audio(audio_path, format="audio/mp3")
            add_to_history("bot", ex, lang_code)

# User input
text = st.text_area("✍️ Enter your own message:")

if st.button("🔊 Generate Speech"):
    if text.strip():
        audio_path = generate_gtts_audio(text, lang_code, slow)
        st.audio(audio_path, format="audio/mp3")
        st.download_button("⬇️ Download Audio", data=open(audio_path, "rb"), file_name="output.mp3", mime="audio/mp3")
        st.session_state.history.append({"role": "user", "text": text})
        add_to_history("user", text, lang_code)
    else:
        st.warning("⚠️ Please enter some text.")

if st.button("🗑️ Clear Session History"):
    st.session_state.history.clear()
