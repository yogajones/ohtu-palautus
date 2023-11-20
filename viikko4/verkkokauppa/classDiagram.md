classDiagram
    class Kauppa {
        - _varasto: Varasto
        - _pankki: Pankki
        - _viitegeneraattori: Viitegeneraattori
        - _kaupan_tili: String
        - _ostoskori: Ostoskori

        + Kauppa(varasto: Varasto, pankki: Pankki, viitegeneraattori: Viitegeneraattori)
        + aloita_asiointi(): void
        + poista_korista(id: int): void
        + lisaa_koriin(id: int): void
        + tilimaksu(nimi: String, tili_numero: String): boolean
    }

    class Ostoskori {
        - _tuotteet: List

        + Ostoskori()
        + lisaa(tuote: Any): void
        + poista(tuote: Any): void
        + hinta(): float
    }

    class Varasto {
        - _kirjanpito: Kirjanpito
        - _saldot: Dict[Tuote, int]

        + Varasto(kirjanpito: Kirjanpito = default_kirjanpito)
        + hae_tuote(id: int): Tuote
        + saldo(id: int): int
        + ota_varastosta(tuote: Tuote): void
        + palauta_varastoon(tuote: Tuote): void
        - _alusta_tuotteet(): void
    }

    class Pankki {
        - _kirjanpito: Kirjanpito

        + Pankki(kirjanpito: Kirjanpito = default_kirjanpito)
        + tilisiirto(nimi: str, viitenumero: str, tililta: str, tilille: str, summa: float): bool
    }

    class Tuote {
        - id: int
        - nimi: str
        - hinta: float

        + Tuote(id: int, nimi: str, hinta: float)
        + __hash__(): int
        + __eq__(other: Any): bool
        + __str__(): str
    }

    class Viitegeneraattori {
        - _seuraava: int

        + Viitegeneraattori()
        + uusi(): int
    }

    class Kirjanpito {
        - tapahtumat: List

        + Kirjanpito()
        + lisaa_tapahtuma(tapahtuma: Any): void
    }
    
    Kauppa <-- Ostoskori
    Kauppa <-- Varasto
    Kauppa <-- Pankki
    Kauppa <-- Viitegeneraattori
    Kauppa <-- Kirjanpito
    Varasto --> Tuote
    Ostoskori --> Tuote