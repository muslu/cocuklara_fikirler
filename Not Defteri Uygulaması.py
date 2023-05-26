def not_defteri():
    while True:
        print("1- Yeni Not")
        print("2- Notları Görüntüle")
        print("3- Çıkış")

        secim = input("Seçiminizi yapın (1-3): ")

        if secim == "1":
            not_ekle()
        elif secim == "2":
            notlari_goruntule()
        elif secim == "3":
            print("Not Defteri kapatılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")

def not_ekle():
    not_metni = input("Yeni notunuzu girin: ")
    with open("notlar.txt", "a") as dosya:
        dosya.write(not_metni + "\n")
    print("Not başarıyla eklendi.")

def notlari_goruntule():
    try:
        with open("notlar.txt", "r") as dosya:
            notlar = dosya.readlines()
            if notlar:
                print("Notlar:")
                for i, not_satiri in enumerate(notlar, 1):
                    print(f"{i}. {not_satiri.strip()}")
            else:
                print("Henüz hiç not eklenmemiş.")
    except FileNotFoundError:
        print("Not defteri bulunamadı.")

not_defteri()
