import pyttsx3


def speak(read_text):
    speaker = pyttsx3.init()
    speaker.say(read_text)
    speaker.runAndWait()
