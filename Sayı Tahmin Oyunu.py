import random

hedef_sayi = random.randint(1, 100)
tahmin_hakki = 5

print("1 ile 100 arasında bir sayıyı tahmin etmeye çalışın.")
print("Tahmin hakkınız:", tahmin_hakki)

while tahmin_hakki > 0:
    tahmin = int(input("Tahmininizi girin: "))

    if tahmin < hedef_sayi:
        print("Daha yüksek bir sayı dene.")
    elif tahmin > hedef_sayi:
        print("Daha düşük bir sayı dene.")
    else:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break

    tahmin_hakki -= 1
    print("Tahmin hakkınız:", tahmin_hakki)

if tahmin_hakki == 0:
    print("Üzgünüm, tahmin hakkınız bitti. Doğru sayı:", hedef_sayi)
