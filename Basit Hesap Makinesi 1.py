def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y

print("Hesap Makinesi")
print("İşlemler: 1- Toplama, 2- Çıkarma, 3- Çarpma, 4- Bölme")

secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")

num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))

if secim == "1":
    sonuc = toplama(num1, num2)
    print("Sonuç:", sonuc)
elif secim == "2":
    sonuc = cikarma(num1, num2)
    print("Sonuç:", sonuc)
elif secim == "3":
    sonuc = carpma(num1, num2)
    print("Sonuç:", sonuc)
elif secim == "4":
    sonuc = bolme(num1, num2)
    print("Sonuç:", sonuc)
else:
    print("Geçersiz bir seçim yaptınız.")
