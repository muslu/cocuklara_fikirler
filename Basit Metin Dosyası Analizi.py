def metin_dosyasi_analizi():
    dosya_adı = input("Analiz edilecek metin dosyasının adını girin: ")

    with open(dosya_adı, "r") as dosya:
        metin = dosya.read()

        kelime_sayısı = len(metin.split())
        cümle_sayısı = metin.count(".") + metin.count("?") + metin.count("!")

        kelimeler = metin.split()
        kelime_frekansları = {}

        for kelime in kelimeler:
            if kelime in kelime_frekansları:
                kelime_frekansları[kelime] += 1
            else:
                kelime_frekansları[kelime] = 1

        en_sık_kelime = max(kelime_frekansları, key=kelime_frekansları.get)

    print("\nMetin Dosyası Analizi Sonuçları:")
    print(f"Kelime Sayısı: {kelime_sayısı}")
    print(f"Cümle Sayısı: {cümle_sayısı}")
    print(f"En Sık Kullanılan Kelime: {en_sık_kelime}")


metin
