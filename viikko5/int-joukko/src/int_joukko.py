KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    """Simuloi ohjelmointikieltä, jossa ei ole valmista tietorakennetta listalle."""
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        try:
            self._validoi_syotteet(kapasiteetti, kasvatuskoko)
        except Exception as e:
            print(f"Virhe syötteessä: {e}")
            return

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkioiden_lkm = 0

        self.lista = self._luo_lista(self.kapasiteetti)

    def _luo_lista(self, koko):
        return [0] * koko

    def _validoi_syotteet(self, kapasiteetti, kasvatuskoko):
        if not isinstance(kapasiteetti, int) or \
            not isinstance(kasvatuskoko, int) or \
                kapasiteetti < 0 or \
                kasvatuskoko < 0:
            raise Exception(
                "kapasiteetin ja kasvatuskoon tulee olla positiivisia kokonaislukuja")

    def kuuluu(self, etsittava_alkio):        
        for i in range(0, self.alkioiden_lkm):
            if self.lista[i] == etsittava_alkio:
                return True
        return False
    
    def _kasvata_kokoa(self):
        taulukko_old = self.lista
        self.kopioi_lista(self.lista, taulukko_old)
        self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.lista)

    def _tilaa(self):
        if self.alkioiden_lkm == len(self.lista):
            return False
        return True

    def _lisaa_alkio(self, alkio):
        self.lista[self.alkioiden_lkm] = alkio
        self.alkioiden_lkm = self.alkioiden_lkm + 1

    def lisaa(self, uusi_alkio):
        if not self.kuuluu(uusi_alkio):
            self._lisaa_alkio(uusi_alkio)
            if not self._tilaa():
                self._kasvata_kokoa()                
            return True
        return False
    
    def _etsi_indeksi(self, alkio):
        indeksi = None
        for i in range(0, self.alkioiden_lkm):
            if alkio == self.lista[i]:
                indeksi = i
                return indeksi
        return indeksi

    def _jarjesta_indeksit(self, alku):
        seuraava = 0
        for i in range(alku, self.alkioiden_lkm):
            seuraava = self.lista[i]
            self.lista[i] = self.lista[i + 1]
            self.lista[i + 1] = seuraava

    def poista(self, poistettava):
        poista_indeksi = self._etsi_indeksi(poistettava)

        if poista_indeksi is not None:
            self.lista[poista_indeksi] = 0
            self.alkioiden_lkm -= 1
            self._jarjesta_indeksit(poista_indeksi) # :D
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lista[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lista[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
