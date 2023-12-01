class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = 0

    def miinus(self, operandi):
        self._aseta_edellinen()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._aseta_edellinen()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._aseta_edellinen()
        self._arvo = 0
    
    def kumoa(self):
        self._arvo = self._edellinen_arvo

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def _aseta_edellinen(self):
        self._edellinen_arvo = self._arvo

    def arvo(self):
        return self._arvo
    
    def edellinen_arvo(self):
        return self._edellinen_arvo
