KAFEER = [                                                           # Lager en liste med 3 ulike kafeer
    {                                                                # Lager en dictionary med nøkkel-par som gjør det enklere å hente ut informasjon
        "id": "optimisten",
        "navn": "Kafé Optimisten",
        "bygg": "Kjølv Egelands hus",
        "apningstid": "08:00–17:30",
        "meny": [
            {"rett": "Varmmatsbuffé", "vegetar": False, "pris": 79},
            {"rett": "Salatbar", "vegetar": True, "pris": 69}
        ]
    },

    {
        "id": "sentralen",
        "navn": "Kafé Sentralen",
        "bygg": "Arne Rettedals hus",
        "apningstid": "08:00–15:00",
        "meny": [
            {"rett": "Suppe", "vegetar": False, "pris": 49},
            {"rett": "Salatbar", "vegetar": True, "pris": 69}
        ]
    },

    {
        "id":"humanisten",
        "navn": "Kafé Humanisten",
        "bygg": "Hulda Garborgs hus",
        "apningstid": "08:00-14:45",
        "meny": [
            {"rett": "Pizza", "vegetar": False, "pris": 59},
            {"rett": "Påsmurt", "vegetar": True, "pris": 49}
        ]
    }
]


def hent_kafe(kafe_id):             
    """Returner dictionary for kafeen med gitt id, eller None hvis den ikke finnes."""
    for kafe in KAFEER:             # Går gjennom KAFEER med en for-løkke.
        if kafe["id"] == kafe_id:   
            return kafe             # Sjekker om det er treff i listen, returner den riktige kafeen
    return None                     # Ingen treff i hele listen, kafeen finnes ikke


def vegetarretter(kafe_id):
    """Returner en liste med navn på vegetarretter for en kafé."""
    veggis = hent_kafe(kafe_id)           # Bruker funksjonen hent_kafe
    if veggis is None:                    # Hvis kafeen ikke finnes, returner tom liste.
        return []
    resultat = []
    for veg in veggis["meny"]:            # Går gjennom kafe["meny"] og samler rettens navn der vegetar er True i en liste.
        if veg["vegetar"] == True:
            resultat.append(veg["rett"])
    return resultat

def rimelige_rett(maks_pris):                  # Lager en funksjon for å finne retter tilpasset mitt budsjett
    """Returner en liste med navn på alle retter som koster maks_pris eller mindre"""
    matpris = []
    for hver_kafe in KAFEER:                   # Går gjennom hver kafe
        for budsjett in hver_kafe["meny"]:     # Går gjennom hver meny i hver kafe
            if budsjett["pris"] <= maks_pris:     
                matpris.append(budsjett["rett"])  # Legger inn rettene som er innenfor budsjettet mitt
    return matpris                             # Returnerer rettene

if __name__ == "__main__":
    print("Antall kafeer:", len(KAFEER))
    print("Optimisten:", hent_kafe("optimisten"))
    print("Finnes ikke:", hent_kafe("finnes-ikke"))
    print("Vegetar Optimisten:", vegetarretter("optimisten"))
    print("Rimelige rett:", rimelige_rett(100))
