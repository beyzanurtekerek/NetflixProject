import speech_recognition as sr
import time
from komutlar import Komut

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("nasıl yardımcı olabilirim beyza")
        audio = r.listen(source)

    voice = ''
    try:
        voice = r.recognize_google(audio, language = "tr-TR")
        print(voice)
        komut = Komut(voice)
        komut.komutBul()
        time.sleep(1)

    except sr.UnknownValueError:
        print("anlamadım")

    except sr.RequestError:
        print("sistem çalışmıyor")


