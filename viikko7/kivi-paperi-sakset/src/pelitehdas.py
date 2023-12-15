from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def uusi_peli(pelikumppani):
    if pelikumppani.endswith("a"):
        return KPSPelaajaVsPelaaja()
    elif pelikumppani.endswith("b"):
        return KPSTekoaly()
    elif pelikumppani.endswith("c"):
        return KPSParempiTekoaly()

    return None


def ohjeet():
    return ("\nTervetuloa pelaamaan kivi-paperi-sakset -peliä!"
            "\n\nValitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"

            "\n\nPaina mitä tahansa muuta näppäintä poistuaksesi ohjelmasta."

            "\n\nPeli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
