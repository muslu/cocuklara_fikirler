def metin_macerasi_oyunu():
    print("Hoş geldiniz! Macera başlasın.")
    # Oyunun devam edeceği döngü
    while True:
        print("Ne yapmak istersiniz?")
        print("a) Mağaraya git")
        print("b) Ormana git")
        print("c) Nehire git")
        print("q) Oyundan çık")

        secim = input("Seçiminizi yapın: ")

        if secim == "a":
            print("Mağaradasınız! Tehlikeli bir yaratıkla karşılaştınız.")
            # Macera olayları devam eder...
        elif secim == "b":
            print("Ormandasınız! Bir hazine buldunuz.")
            # Macera olayları devam eder...
        elif secim == "c":
            print("Nehirdesiniz! Yüzebilirsiniz.")
            # Macera olayları devam eder...
        elif secim == "q":
            print("Oyundan çıkılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")

metin_macerasi_oyunu()
