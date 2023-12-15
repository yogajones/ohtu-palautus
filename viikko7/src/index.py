from pelitehdas import ohjeet, uusi_peli


def main():
    while True:
        print(ohjeet())

        pelikumppani = input()
        peli = uusi_peli(pelikumppani)  # gganbu :D

        if peli is None:
            break

        peli.pelaa()


if __name__ == "__main__":
    main()
