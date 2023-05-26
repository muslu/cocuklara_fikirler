def tic_tac_toe():
    tahta = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    siradaki_oyuncu = "X"
    oyun_devam_ediyor = True

    def tahtayi_goster():
        print("\n")
        for satir in tahta:
            print(" | ".join(satir))
            print("---------")

    def hamle_yap():
        while True:
            satir = int(input("Satır numarasını girin (1-3): ")) - 1
            sutun = int(input("Sütun numarasını girin (1-3): ")) - 1

            if satir in range(3) and sutun in range(3) and tahta[satir][sutun] == " ":
                tahta[satir][sutun] = siradaki_oyuncu
                break
            else:
                print("Geçersiz hamle. Lütfen tekrar deneyin.")

    def kazanan_mi():
        # Satırları kontrol et
        for satir in tahta:
            if satir[0] == satir[1] == satir[2] != " ":
                return True

        # Sütunları kontrol et
        for sutun in range(3):
            if tahta[0][sutun] == tahta[1][sutun] == tahta[2][sutun] != " ":
                return True

        # Çaprazları kontrol et
        if tahta[0][0] == tahta[1][1] == tahta[2][2] != " ":
            return True

        if tahta[0][2] == tahta[1][1] == tahta[2][0] != " ":
            return True

        return False

    def berabere_mi():
        for satir in tahta:
            if " " in satir:
                return False
        return True

    while oyun_devam_ediyor:
        tahtayi_goster()
        print(f"Sıra: {siradaki_oyuncu}")

        hamle_yap()

        if kazanan_mi():
            tahtayi_goster()
            print(f"Oyunu {siradaki_oyuncu} kazandı!")
            oyun_devam_ediyor = False
        elif berabere_mi():
            tahtayi_goster()
            print("Oyun berabere!")
            oyun_devam_ediyor = False
        else:
            if siradaki_oyuncu == "X":
                siradaki_oyuncu = "O"
            else:
                siradaki_oyuncu = "X"


tic_tac_toe()
