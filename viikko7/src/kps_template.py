from tuomari import Tuomari


class KPS:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._validoi_siirrot(ekan_siirto, tokan_siirto):
            tuomari.kirjaa_siirrot(ekan_siirto, tokan_siirto)
            print(tuomari)
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"

    def _validoi_siirrot(self, ekan_siirto, tokan_siirto):
        return ekan_siirto in ("k", "p", "s") and tokan_siirto in ("k", "p", "s")
