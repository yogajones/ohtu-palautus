import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 8)
            if tuote_id == 3:
                return Tuote(3, "leipä", 2)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa_mock = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # aloitetaan asiointi
        self.kauppa_mock.aloita_asiointi()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatytyya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        
        # tehdään ostokset
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi.return_value, "12345", ANY, 5)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_kaksi_eri_tuotetta(self):
        
        # tehdään ostokset kahdella eri tuotteella
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.lisaa_koriin(2)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi.return_value, "12345", ANY, 13)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_kaksi_samaa_tuotetta(self):

        # tehdään ostokset kahdella samalla tuotteella

        self.kauppa_mock.lisaa_koriin(2)
        self.kauppa_mock.lisaa_koriin(2)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi.return_value, "12345", ANY, 16)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_toinen_tuote_loppu(self):

        # tehdään ostokset, toinen tuote (id=3) on loppu
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.lisaa_koriin(3)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että tililtä lähdetään veloittamaan vain jäljellä olevan tuotteen summaa
        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi.return_value, "12345", ANY, 5)