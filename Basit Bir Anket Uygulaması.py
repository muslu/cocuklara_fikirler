def anket():
    sorular = ["En sevdiğiniz renk nedir?", "En sevdiğiniz hayvan nedir?", "En sevdiğiniz yemek nedir?"]
    cevaplar = []

    for soru in sorular:
        cevap = input(soru + " ")
        cevaplar.append(cevap)

    print("\nAnket Sonuçları:")
    for i in range(len(sorular)):
        print(sorular[i], cevaplar[i])


anket()
