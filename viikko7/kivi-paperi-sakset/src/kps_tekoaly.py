from tekoaly import Tekoaly
from kps_template import KPS


class KPSTekoaly(KPS):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
