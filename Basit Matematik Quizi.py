import random

dogru_cevaplar = 0
soru_sayisi = 5

for _ in range(soru_sayisi):
    sayi1 = random.randint(1, 10)
    sayi2 = random.randint(1, 10)
    islemler = ["+", "-", "*"]
    islem = random.choice(islemler)

    if islem == "+":
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    else:
        sonuc = sayi1 * sayi2

    soru = f"{sayi1} {islem} {sayi2} = "

    cevap = int(input(soru))

    if cevap == sonuc:
        print("Tebrikler, doğru cevap!")
        dogru_cevaplar += 1
    else:
        print("Üzgünüm, yanlış cevap.")

basari_orani = (dogru_cevaplar / soru_sayisi) * 100
print(f"\nBaşarı oranınız: {basari_orani}%")
