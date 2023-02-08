import playsound
from gtts import gTTS

#function to implement speech to text functionality
def speak(text):
    tts = gTTS(text = text,lang='en', tld="com")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

