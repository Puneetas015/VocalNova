import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        audio = recognizer.listen(mic)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        return "Could not understand audio"
