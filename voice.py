import speech_recognition as sr
from text import *
r = sr.Recognizer()

#function to implement speech to text application
def voice():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak("Speak Now")
        audio = r.listen(source)
        voice_message = r.recognize_google(audio)
        return voice_message
 
 
 
 