# Hesap bilgileri tutulacak. (dict) veri tabanı mahiyetinde
hesaplar = {
    8978 : {
        "ad":"Mücahit Üstüner",
        "bakiye": 17000000,
        "ekHesap": 200000,
        "username": "mucahitustuner",
        "password":"12345"    
    },
    5876 : {
        "ad":"Çınar Üstüner",
        "bakiye": 170000,
        "ekHesap": 1700,
        "username": "çınarustuner",
        "password":"54321"       
    }
}


def login():
    while True:
        username = input("username: ")
        password = input("parola: ")
        accountNumber = int(input("account number: "))
        check = hesaplar.get(accountNumber)

        if check:
            if check["username"] == username and check["password"] == password:
                menu(check) #giriş yapıldıysa menü gelsin.
                break # hesap uyuşuyorsa sonraki hesaplara bakmayı bırak deriz
            else:
                print("username yada parola yanlış. Lütfen tekrar kontrol edin")

        else:
            print("Hesap numarasını tekrar kontrol edin")
            login() #bilgiler yanlış girilince bilgilendirip tekrar login olsun.



def menu(hesap):
    while True:

        print("\n")
        print(f"Merhaba, {hesap["ad"]}") #kullanıcıyı sözlükten aldığımız ad ile selamladık

        print("1- Bakiye Sorgulama") # ilk bilgilendirme yapacağız
        print("2- Para Çekme")
        print("3- Para Yatırma")
        print("4- Çıkış")
        tus = int(input("Yapmak istediğiniz işlemi tuşlayınız: "))

        if tus == 1:
            bakiyeSorgula(hesap) #eğer 1'e basarsa bakiyesorgula fonksiyonunu çağır referas olarak hesap
        elif tus == 2:
            paraCekme(hesap)
        elif tus == 3:
            paraYatirma(hesap)
        elif tus == 4:
            break
        else:
            print("Yanlış tuşlama.") #mutlaka aksi durum için bir cevabımız olmalı
            continue
    
        x = input("Başka bir işlem yapmak istiyormusunuz?  (E/H)").lower()
        if x == "e":
            continue
        else:
            print(f" {hesap["ad"]} iyi günler dileriz ")
            break




def paraCekme(hesap):
    miktar = float(input("çekmek istdiğiniz miktarı giriniz: "))
    if hesap["bakiye"] >= miktar: #eğer çekilecek miktar bakiyeden küçükse...
        hesap["bakiye"] -= miktar #çekilecek miktarı bakiyeden eksilt
        print("Paranızı alabilirsiniz")
    else:
        toplam = hesap["bakiye"]  + hesap["ekHesap"]
        if toplam >= miktar:
            ekhesapcekimi = input("ek hesap kullanılsın mı? (e/h): ")
            if ekhesapcekimi == "e": # e dışında herhangi tuşa basarsa ek hesap çekimi iptal olur if bloğu çalışmaz
                kullanilacakMiktar = miktar - hesap["bakiye"] #bakiyemizi zaten yetersiz burada 0 lıyoruz
                hesap["bakiye"] = 0 #bakiyemizi yukarda 0'ladık kalanı ek hesaptan alacağız
                hesap["ekHesap"] -= kullanilacakMiktar
                print("paranızı alabilirsiniz")
            else:
                print("ek hesap çekiminiz iptal edildi.")
        else:
            print("üzgünüz bakiyeniz yetersiz")



def bakiyeSorgula(hesap):
    print(f"Bakiyeniz: {hesap["bakiye"]}")
    print(f"Ek bakiyeniz: {hesap["ekHesap"]}")

def paraYatirma(hesap):
    yatir = int(input("yatırılacak tutarı girin: "))
    hesap["bakiye"] += yatir
    print(f"{yatir} tl hesabınıza yatırıldı. Güncel bakiyeniz: {hesap["bakiye"]}")


login()
