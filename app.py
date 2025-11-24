import streamlit as st
import base64
import tempfile
import threading
from nlp import get_reply
from tts import speak_text, stop_speech

st.set_page_config(page_title="AI Voice Bot", layout="centered")

st.title("🎤 AI Voice Bot (Gemini 2.5 Flash)")

# ---- SESSION STATE ----
if "chat" not in st.session_state:
    st.session_state.chat = []

if "speaking_thread" not in st.session_state:
    st.session_state.speaking_thread = None


# ---- SIDEBAR ----
with st.sidebar:
    st.header("⚙ Controls")
    if st.button("🛑 Stop Speaking"):
        stop_speech()
        st.warning("Voice stopped!")



# ---- MIC INPUT ----
audio_data = st.audio_input("🎙 Speak here")

user_text = st.text_input("Or type your message:")

if st.button("Ask"):
    final_input = ""

    # mic input
    if audio_data is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio_data.getvalue())
            audio_path = temp_audio.name

        try:
            import speech_recognition as sr
            r = sr.Recognizer()
            with sr.AudioFile(audio_path) as source:
                audio_listened = r.record(source)
                final_input = r.recognize_google(audio_listened)
        except:
            st.error("Speech recognition failed")

    # typed input
    if user_text:
        final_input = user_text

    if final_input == "":
        st.warning("Please speak or type something.")
    else:
        st.session_state.chat.append(("user", final_input))

        reply = get_reply(final_input)
        st.session_state.chat.append(("bot", reply))

        # play speech in background thread
        t = threading.Thread(target=speak_text, args=(reply,))
        t.start()
        st.session_state.speaking_thread = t


# ---- CHAT DISPLAY ----
st.write("### 🗨 Chat History")

for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"<div style='background:#007AFF22;padding:10px;border-radius:8px;margin:5px;'><b>🧑 You:</b> {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background:#00C85322;padding:10px;border-radius:8px;margin:5px;'><b>🤖 Bot:</b> {msg}</div>", unsafe_allow_html=True)
