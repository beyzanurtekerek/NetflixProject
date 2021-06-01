from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import webbrowser as wb
import pyautogui
import sqlite3

con = sqlite3.connect("sesliasistan.db")
cursor = con.cursor()
dosya = open("sesliasistan.txt", "a")


def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS sesler (komut TEXT)")
    con.commit()
    con.close()
tablo()

class Komut():
    def __init__(self,gelenSes):
        self.ses = gelenSes.upper()
        self.kelimeler = self.ses.split()
        print(self.kelimeler)
        self.komutlar = ['NE HABER', 'NASILSIN', 'KAPAT', 'GİRİŞ','NETFLİX', 'BEYZA', 'ANA SAYFA', 'DİZİLER',
                         'FİLMLER', 'LİSTEM', 'GERİ', 'İLERİ', 'OYNAT', 'BİR AŞAĞI', 'İKİ AŞAĞI',
                         'BİRİ İZLE', 'BİRİ OYNAT' ,'İKİYİ İZLE', 'İKİYİ OYNAT', 'ÇIK']

    def seslendirme(self,yazi):
        tts = gTTS(text = yazi, lang="tr")
        rand = random.randint(1, 10000)
        file = "audio-" + str(rand) + ".mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)
        print(text)

    def sohbet(self):
        sozler = ["iyiyim sen nasılsın?",
                  "benim duygularım yok ama sanırım insanlar bu soruya iyiyim diyor",
                  "fıstık gibiyim sen nasılsın?",
                  "çok iyiyim canım",
                  "iyilik, güzellik. senin için ne yapabilirim?"]
        secim = choice(sozler)
        self.seslendirme(secim)
        dosya.write("komut: nasılsın/naber")
        tablo()
        cursor.execute("INSERT INTO sesler VALUE('naber')")
        con.commit()
        con.close()


    def giris(self):
        self.seslendirme("Hoş geldin! Lütfen Netflix'e giriş yap.")
        cursor.execute("INSERT INTO sesler VALUE('giriş')")
        con.commit()
        con.close()

        while True:
            mailAdress = input("Mail adresiniz: ")
            password = input("Şifreniz: ")

            if mailAdress == "beyzanurtekerk@gmail.com" and password != gizli.sifre:
                print("Şifre hatalı. Uyarı maili gönderiliyor...")
                try:
                    # mail bilgileri
                    subject = "Güvenlik uyarısı"
                    message = "Beyza Nur, hesabına hatalı giriş tespit ettik."
                    content = "Subject: {0}\n{1}".format(subject, message)

                    # netflix hesap bilgileri
                    myMailAdress = "netflixproje@gmail.com"
                    myPassword = gizli.sifre  # sifreyi baska bir dosyada tuttum

                    # kime gönderilecek (kullanıcıya)
                    sendTo = "beyzanurtekerk@gmail.com"
                    mail = SMTP("smtp.gmail.com", 587)  # gmailin host adresini ve kullandıgı hizmet numarasını girdim
                    mail.ehlo()  # baglantı islemini gerceklestirdim
                    mail.starttls()  # verileri sifreli bir sekilde göndermek icin
                    mail.login(myMailAdress, myPassword)  # oturum actık
                    mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))  # kimden, kime, mesaj
                    print(
                        "Güvenlik uyarısı maili gönderildi. Tekrar deneyin.\n--------------------------------------------------")
                except Exception as i:
                    print("Mail gönderilirken bir hata oluştu! Tekrar deneyin.\n{0}".format(i))
                continue
            elif mailAdress == "beyzanurtekerk@gmail.com" and password == gizli.sifre:
                print("Netflix'e hoş geldin!")
                break
            else:
                print("Böyle bir hesap yok! Tekrar deneyin.\n--------------------------------------------------")
                continue

    def netflix(self):
        url = "https://netflix.com/"
        new = 0  # sekmeyi nasıl acacagını belirliyor
        autoraise = True
        wb.open(url, new, autoraise)
        dosya.write("komut: netflix")
        cursor.execute("INSERT INTO sesler VALUE('netflix')")
        con.commit()
        con.close()

    def beyza(self):
        pyautogui.click(x = 723, y = 517)
        dosya.write("komut: beyza")
        cursor.execute("INSERT INTO sesler VALUE('beyza')")
        con.commit()
        con.close()

    def anasayfa(self):
        pyautogui.click(x = 333, y = 163)
        dosya.write("komut: anasayfa")
        cursor.execute("INSERT INTO sesler VALUE('ana sayfa')")
        con.commit()
        con.close()

    def diziler(self):
        pyautogui.click(x = 432, y = 152)
        dosya.write("komut: diziler")
        cursor.execute("INSERT INTO sesler VALUE('diziler')")
        con.commit()
        con.close()

    def filmler(self):
        pyautogui.click(x = 525, y = 151)
        dosya.write("komut: filmler")
        cursor.execute("INSERT INTO sesler VALUE('filmler')")
        con.commit()
        con.close()

    def listem(self):
        pyautogui.click(x = 797, y = 163)
        dosya.write("komut: listem")
        cursor.execute("INSERT INTO sesler VALUE('listem')")
        con.commit()
        con.close()

    def geri(self):
        pyautogui.click(x = 31, y = 77)
        dosya.write("komut: geri")
        cursor.execute("INSERT INTO sesler VALUE('geri')")
        con.commit()
        con.close()

    def ileri(self):
        pyautogui.click(x = 81, y = 77)
        dosya.write("komut: ileri")
        cursor.execute("INSERT INTO sesler VALUE('ileri')")
        con.commit()
        con.close()

    def oynat(self):
        pyautogui.click(x = 172, y = 765)
        dosya.write("komut: oynat")
        cursor.execute("INSERT INTO sesler VALUE('oynat')")
        con.commit()
        con.close()

    def birAlt(self):
        pyautogui.click(x = 1907, y = 400)
        dosya.write("komut: bir aşağı")
        cursor.execute("INSERT INTO sesler VALUE('bir aşağı')")
        con.commit()
        con.close()

    def ikiAlt(self):
        pyautogui.click(x = 1907, y = 584)
        dosya.write("komut: iki aşağı")
        cursor.execute("INSERT INTO sesler VALUE('iki aşağı')")
        con.commit()
        con.close()

    def videoBir(self):
        pyautogui.click(x = 235, y = 690)
        dosya.write("komut: biri izle")
        cursor.execute("INSERT INTO sesler VALUE('biri izle')")
        con.commit()
        con.close()

    def videoİki(self):
        pyautogui.click(x = 590, y = 676)
        dosya.write("komut: ikiyi izle")
        cursor.execute("INSERT INTO sesler VALUE('ikiyi izle')")
        con.commit()
        con.close()

    def biriAc(self):
        pyautogui.click(x = 127, y = 652)
        dosya.write("komut: biri oynat")
        cursor.execute("INSERT INTO sesler VALUE('biri oynat')")
        con.commit()
        con.close()

    def ikiyiAc(self):
        pyautogui.click(x = 391, y = 650)
        dosya.write("komut: ikiyi oynat")
        cursor.execute("INSERT INTO sesler VALUE('ikiyi oynat')")
        con.commit()
        con.close()

    def cik(self):
        pyautogui.click(x = 1884, y = 22)
        dosya.write("komut: çık")
        cursor.execute("INSERT INTO sesler VALUE('çık')")
        con.commit()
        con.close()

    def kapat(self):
        self.seslendirme("tamamdır kapatıyorum")
        dosya.write("komut: kapat")
        cursor.execute("INSERT INTO sesler VALUE('kapat')")
        con.commit()
        con.close()
        sys.exit()

    def komutBul(self):
        for komut in self.komutlar:
            if komut in self.kelimeler:
                calistir(komut)

    def calistir(self):
        if komut == 'NE HABER' or komut == 'NASILSIN':
            self.sohbet()
        if komut == 'KAPAT':
            self.kapat()
        if komut == 'GİRİŞ':
            self.giris()
        if komut == 'NETFLİX':
            self.netflix()
        if komut == 'BEYZA':
            self.beyza()
        if komut == 'ANA SAYFA':
            self.anasayfa()
        if komut == 'DİZİLER':
            self.diziler()
        if komut == 'FİLMLER':
            self.filmler()
        if komut == 'LİSTEM':
            self.listem()
        if komut == 'GERİ':
            self.geri()
        if komut == 'İLERİ':
            self.ileri()
        if komut == 'OYNAT':
            self.oynat()
        if komut == 'BİR AŞAĞI':
            self.birAlt()
        if komut == 'İKİ AŞAĞI':
            self.ikiAlt()
        if komut == 'BİRİ İZLE':
            self.videoBir()
        if komut == 'İKİYİ İZLE':
            self.videoİki()
        if komut == 'BİRİ OYNAT':
            self.biriAc()
        if komut == 'İKİYİ OYNAT':
            self.ikiyiAc()
        if komut == 'ÇIK':
            self.cik()
dosya.close()