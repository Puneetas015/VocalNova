from gtts import gTTS
import simpleaudio as sa
import tempfile
import os

current_playback = None  # global audio handler


def speak_text(text):
    global current_playback

    # Convert text to speech
    tts = gTTS(text=text, lang="en")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        temp_path = f.name
        tts.save(temp_path)

    # Load & play audio using simpleaudio
    wave_obj = sa.WaveObject.from_wave_file(convert_mp3_to_wav(temp_path))
    current_playback = wave_obj.play()  # non-blocking play

    current_playback.wait_done()  # allow stop to interrupt

    # Cleanup
    try:
        os.remove(temp_path)
        os.remove(temp_path + ".wav")
    except:
        pass


def stop_speech():
    global current_playback
    if current_playback and current_playback.is_playing():
        current_playback.stop()
        current_playback = None


def convert_mp3_to_wav(mp3_path):
    """Convert mp3 → wav because simpleaudio does not play mp3."""
    from pydub import AudioSegment
    sound = AudioSegment.from_mp3(mp3_path)
    wav_path = mp3_path + ".wav"
    sound.export(wav_path, format="wav")
    return wav_path
