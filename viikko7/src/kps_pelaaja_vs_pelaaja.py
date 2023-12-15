from kps_template import KPS


class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")
