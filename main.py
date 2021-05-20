from smtplib import SMTP   # simple mail transfer protocol
import gizli
import speech_recognition as sr
from gtts import gTTS   # google text to speech
from playsound import playsound
import webbrowser
import time
import random
import os

r = sr.Recognizer()
def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language = "tr-TR")
        except sr.UnknownValueError:
            speak("anlamadım")
        except sr.RequestError:
            speak("sistem çalışmıyor")
        return voice

def response(voice):
    if 'nasılsın' in voice:
        speak("merhaba beyza iyiyim")
    if 'arama' in voice:
        search = record("ne aramak istiyorsun")
        url = "https://google.com/search?q=" + search
        webbrowser.open(url)
        speak(search + "için bulduklarım")
    if 'görüşürüz' in voice:
        speak("görüşürüz")
    exit()

def speak(string):
    tts = gTTS(string, lang = "tr")
    rand = random.randint(1,10000)
    file = "audio-" + str(rand) + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("nasıl yardımcı olabilirim beyza")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)

# ilk log in olacak
"""speak("Hoş geldin! Lütfen Netflix'e giriş yap.")

while True:
    mailAdress = input("Mail adresiniz: ")
    password = input("Şifreniz: ")

    if mailAdress == "beyzanurtekerk@gmail.com" and password != gizli.sifre:
        print("Şifre hatalı. Uyarı maili gönderiliyor...")
        try:
            # mail bilgileri
            subject = "Güvenlik uyarısı"
            message = "Beyza Nur, hesabına hatalı giriş tespit ettik."
            content = "Subject: {0}\n{1}".format(subject,message)

            # netflix hesap bilgileri
            myMailAdress = "netflixproje@gmail.com"
            myPassword = gizli.sifre

            # kime gönderilecek (kullanıcıya)
            sendTo = "beyzanurtekerk@gmail.com"
            mail = SMTP("smtp.gmail.com", 587)                            # gmailin host adresini ve kullandıgı hizmet numarasını girdim
            mail.ehlo()                                                   # baglantı islemini gerceklestirdim
            mail.starttls()                                               # verileri sifreli bir sekilde göndermek icin
            mail.login(myMailAdress, myPassword)                          # oturum actık
            mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))  # kimden, kime, mesaj
            print("Güvenlik uyarısı maili gönderildi. Tekrar deneyin.\n--------------------------------------------------")
        except Exception as i:
            print("Mail gönderilirken bir hata oluştu! Tekrar deneyin.\n{0}".format(i))
        continue
    elif mailAdress == "beyzanurtekerk@gmail.com" and password == gizli.sifre:
        print("Netflix'e hoş geldin!")
        break
    else:
        print("Böyle bir hesap yok! Tekrar deneyin.\n--------------------------------------------------")
        continue"""

