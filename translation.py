import io
import textwrap
from gtts import gTTS
from deep_translator import GoogleTranslator

def translate_text(text, src, target_lang):
    chunks = textwrap.wrap(text, 500)
    translated_chunks = [GoogleTranslator(source=src, target=target_lang).translate(chunk) for chunk in chunks]
    return ' '.join(translated_chunks)

def generate_audio(text, lang):
    if not text:
        raise ValueError("No text to speak.")
    languages = {"English": "en", "Hindi": "hi", "Marathi": "mr", "Bengali": "bn", "Gujarati": "gu",
                 "Telugu": "te", "Tamil": "ta", "Malayalam": "ml", "Kannada": "kn", "Punjabi": "pa"}
    #lang_code = languages.get(lang, "en")
    tts = gTTS(text=text, lang=lang)
    audio_io = io.BytesIO()
    tts.write_to_fp(audio_io)
    audio_io.seek(0)
    return audio_io
