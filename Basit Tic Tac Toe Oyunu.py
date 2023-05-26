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
