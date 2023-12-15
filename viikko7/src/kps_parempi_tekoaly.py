from tekoaly_parannettu import TekoalyParannettu
from kps import KPS


class KPSParempiTekoaly(KPS):
    def __init__(self, muistin_koko) -> None:
        super().__init__()
        self._tekoaly = TekoalyParannettu(muistin_koko)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tokan_siirto
