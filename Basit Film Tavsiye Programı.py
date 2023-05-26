def film_tavsiye():
    print("Film Tavsiye Programına Hoş Geldiniz!")

    favori_filmler = ["The Shawshank Redemption", "The Godfather", "Pulp Fiction", "The Dark Knight",
                      "Fight Club", "Inception", "Goodfellas", "The Matrix", "The Lord of the Rings", "Interstellar"]

    while True:
        print("\n1 - Rastgele Film Tavsiyesi Al")
        print("2 - Favori Filmleri Görüntüle")
        print("3 - Çıkış")

        secim = input("Bir işlem seçin (1-3): ")

        if secim == "1":
            film = random.choice(favori_filmler)
            print(f"\nSize tavsiye edilen film: {film}")

        elif secim == "2":
            print("\nFavori Filmleriniz:")
            for film in favori_filmler:
                print(film)

        elif secim == "3":
            break

        else:
            print("Geçersiz bir seçim yaptınız.")


film_tavsiye()
