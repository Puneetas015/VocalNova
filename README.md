# **AI Voice Bot (Streamlit + Gemini 2.5 Flash)**

This project is a fully interactive AI Voice Assistant built using **Streamlit**, **Google Gemini 2.5 Flash**, **speech-to-text**, and **text-to-speech**.  
You can talk to the assistant using your microphone or type your question.  
It responds with intelligent answers and can speak the reply aloud.  
A **STOP button** is also included so users can interrupt speech anytime. 🔊🛑

---

## **Features**

- **Voice Input**: Speak directly using your microphone.  
- **Text Input**: Type queries manually.  
- **AI Responses**: Powered by Gemini 2.5 Flash for fast + accurate answers.  
- **Text-to-Speech**: Bot reads the response aloud using gTTS.  
- **Stop Speaking Button**: Instantly stop long audio replies.  
- **Chat History**: Clean, session-based chat display.  
- **Streamlit UI**: Simple, elegant browser interface.

---

## **Project Structure**

Below is the complete project file structure in **one place** exactly as you wanted:
```text
voice-bot/
│── app.py → Main Streamlit application
│── nlp.py → Handles Gemini model responses
│── tts.py → Text-to-speech + STOP functionality
│── config.py → Loads environment variables
│── requirements.txt → Python dependencies
│── .gitignore → Prevents sensitive/temporary files from uploading
│── .env → Your API Key (DO NOT upload to GitHub)
```

