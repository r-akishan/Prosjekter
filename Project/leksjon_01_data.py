# =============================================================================
# LEKSJON 1 — Data først, API etterpå
#
# Mål: Du skal kunne forklare (høyt, med egne ord):
#   1. Hva en dictionary er, og hvorfor den passer til kafédata
#   2. Forskjellen på en liste og en dictionary
#   3. Hva funksjonen hent_kafe gjør, linje for linje
#
# Regel: Fyll inn alt merket TODO. Ikke be meg om ferdig fasit
# før du har prøvd. Kjør filen med:
#   python3 "Project/leksjon_01_data.py"
# =============================================================================

# Én kafé som eksempel. Les denne til du skjønner hvert felt.
KAFEER = [
    {
        "id": "optimisten",
        "navn": "Kafé Optimisten",
        "bygg": "Kjølv Egelands hus",
        "apningstid": "08:00–17:30",
        "meny": [
            {"rett": "Varmmatsbuffé", "vegetar": False, "pris": 79},
            {"rett": "Salatbar", "vegetar": True, "pris": 69},
        ],
    },
    # TODO 1: Legg inn Kafé Sentralen med samme felter som Optimisten
    #         (id, navn, bygg, apningstid, meny). Minst 2 retter.
    # TODO 2: Legg inn Kafé Humanisten på samme måte.
]


def hent_kafe(kafe_id):
    """Returner dictionary for kafeen med gitt id, eller None hvis den ikke finnes."""
    # TODO 3: Gå gjennom KAFEER med en for-løkke.
    #         Hvis kafe["id"] == kafe_id, returner den kafeen.
    #         Hvis løkken er ferdig uten treff, returner None.
    pass


def vegetarretter(kafe_id):
    """Returner en liste med navn på vegetarretter for en kafé."""
    # TODO 4: Bruk hent_kafe. Hvis kafeen ikke finnes, returner tom liste.
    #         Gå gjennom kafe["meny"] og samle rett-navn der vegetar er True.
    pass


if __name__ == "__main__":
    # Når TODO-ene er gjort, skal dette gi mening når du kjører filen.
    print("Antall kafeer:", len(KAFEER))
    print("Optimisten:", hent_kafe("optimisten"))
    print("Finnes ikke:", hent_kafe("finnes-ikke"))
    print("Vegetar Optimisten:", vegetarretter("optimisten"))
