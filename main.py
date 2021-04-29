from smtplib import SMTP   # simple mail transfer protocol
import gizli

# ilk log in olacak
print("Hoş geldin! Lütfen Netflix'e giriş yap.")

mailAdress = input(print("Mail adresiniz: "))
password = input(print("Şifreniz: "))

if mailAdress == "beyzanurtekerk@gmail.com" and password != gizli.sifre:
    print("Şifre hatalı.")
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
        mail = SMTP("smtp.gmail.com", 587)  # gmailin host adresini ve kullandıgı hizmet numarasını girdim
        mail.ehlo()  # baglantı islemini gerceklestirdim
        mail.starttls()  # verileri sifreli bir sekilde göndermek icin
        mail.login(myMailAdress, myPassword)  # oturum actık
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))  # kimden, kime, mesaj
        print("Güvenlik uyarısı maili gönderildi.")
    except Exception as i:
        print("Mail gönderilirken bir hata oluştu!\n{0}".format(i))

elif mailAdress == "beyzanurtekerk@gmail.com" and password == gizli.sifre:
    print("Netflix girişin başarılı!")
else:
    print("Böyle bir hesap yok.")



