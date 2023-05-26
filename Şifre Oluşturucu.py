import random
import string

def sifre_olustur():
    uzunluk = int(input("Şifrenin uzunluğunu girin: "))

    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))

    print("Oluşturulan Şifre:", sifre)

sifre_olustur()
