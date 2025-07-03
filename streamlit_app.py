import streamlit as st
from gtts import gTTS
import tempfile

def generate_gtts_audio(text, lang):
    tts = gTTS(text=text, lang=lang)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

# Custom CSS styling with purple gradient on radio options
st.markdown("""
    <style>
        /* Gradient background: light purple to white vertical */
             body, .stApp {
            background: linear-gradient(180deg, #9e92de 0%, #f5f3ff 100%);
            min-height: 100vh;
            color: #000000 !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            transition: background 0.5s ease;
        }

        /* Title styling */
        h1 {
            color: #4B3FA7;  /* darker purple */
            text-align: center;
            margin-top: 1rem;
            font-weight: 700;
            text-shadow: 0 1px 3px rgba(0,0,0,0.1);
            transition: color 0.3s ease;
        }

        /* Main card with mica-glass effect */
        .tts-card {
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 8px 20px rgba(75, 63, 167, 0.25);
            max-width: 700px;
            margin: 2rem auto;
            transition: box-shadow 0.3s ease, transform 0.3s ease;
        }
        .tts-card:hover {
            box-shadow: 0 12px 30px rgba(75, 63, 167, 0.4);
            transform: translateY(-5px);
        }

        /* TextArea: black text on white background */
        .stTextArea textarea {
            color: #000 !important;
            background-color: #fff !important;
            border-radius: 12px !important;
            border: 1.5px solid #4B3FA7 !important;
            padding: 0.75rem !important;
            font-size: 1rem !important;
            transition: border-color 0.3s ease;
        }
        .stTextArea textarea:focus {
            border-color: #7b6df5 !important;
            outline: none !important;
            box-shadow: 0 0 8px #7b6df5;
        }

        /* Buttons styling */
        .stButton > button, .stDownloadButton > button {
            background: linear-gradient(90deg, #7b6df5 0%, #6A5ACD 100%);
            color: #fff !important;
            font-weight: 600;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            cursor: pointer;
            transition: background 0.4s ease, box-shadow 0.3s ease;
            box-shadow: 0 3px 8px rgba(106, 90, 205, 0.4);
        }
        .stButton > button:hover, .stDownloadButton > button:hover {
            background: linear-gradient(90deg, #6A5ACD 0%, #7b6df5 100%);
            box-shadow: 0 5px 15px rgba(123, 109, 245, 0.7);
        }

        /* Audio player margin */
        .stAudio {
            margin-top: 1rem;
        }

        /* Radio group main label ("🌐 Choose language:") stays black */
        div[role="radiogroup"] > label:first-of-type {
            color: #000000 !important;
            font-weight: 600;
            font-size: 1rem;
        }

        /* Radio option labels ("English", "Arabic", "French") purple gradient */
        div[role="radiogroup"] > div > label {
            background: linear-gradient(90deg, #7b6df5 0%, #9a8fff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 600 !important;
            font-size: 0.95rem;
        }

        /* TextArea label ("✍️ Enter your own text:") */
        label[for^="stTextArea"] {
            color: #000000 !important;
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 0.25rem;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎤 Text-to-Speech Generator")

# Wrapper card
with st.container():
    st.markdown('<div class="tts-card">', unsafe_allow_html=True)

    # Language selection
    language = st.radio("🌐 Choose language:", ("English", "Arabic", "French"))

    # Examples per language
    english_examples = [
        "Thank you for contacting customer support. How can we assist you today?",
        "We apologize for the inconvenience caused. Your issue will be resolved as soon as possible.",
        "Please provide your account number, and we'll check the status of your request.",
        "Can you please confirm your email address for verification?",
        "Thank you for your patience. We are processing your request and will update you shortly."
    ]

    arabic_examples = [
        "شكرًا لتواصلك مع دعم العملاء. كيف يمكننا مساعدتك اليوم؟",
        "نعتذر عن الإزعاج الذي تسببت فيه المشكلة. سيتم حلها في أقرب وقت ممكن.",
        "من فضلك قدم لنا رقم حسابك، وسنقوم بالتحقق من حالة طلبك.",
        "هل يمكنك تأكيد عنوان بريدك الإلكتروني للتحقق؟",
        "شكرًا لصبرك. نحن نعمل على معالجة طلبك وسنوافيك بالتحديثات قريبًا."
    ]

    french_examples = [
        "Merci d'avoir contacté notre support client. Comment pouvons-nous vous assister aujourd'hui?",
        "Nous nous excusons pour les désagréments causés. Votre problème sera résolu dans les plus brefs délais.",
        "Veuillez fournir votre numéro de compte, et nous vérifierons l'état de votre demande.",
        "Pouvez-vous confirmer votre adresse e-mail pour vérification?",
        "Merci de votre patience. Nous traitons votre demande et vous tiendrons informé sous peu."
    ]

    # Language logic
    if language == "English":
        examples = english_examples
        lang_code = 'en'
    elif language == "Arabic":
        examples = arabic_examples
        lang_code = 'ar'
    elif language == "French":
        examples = french_examples
        lang_code = 'fr'

    # Display examples with play buttons
    st.markdown("💬 **Try Example Sentences:**")
    for example in examples:
        if st.button(f"▶️ {example}"):
            audio_path = generate_gtts_audio(example, lang_code)
            st.audio(audio_path, format="audio/mp3")

    # User input
    user_input = st.text_area("✍️ Enter your own text:")

    # Generate speech button
    if st.button("🔊 Generate Speech"):
        if user_input.strip():
            audio_path = generate_gtts_audio(user_input, lang_code)
            st.audio(audio_path, format="audio/mp3")
            with open(audio_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Audio",
                    data=f,
                    file_name="output_audio.mp3",
                    mime="audio/mp3"
                )
        else:
            st.warning("⚠️ Input something!")

    st.markdown('</div>', unsafe_allow_html=True)
