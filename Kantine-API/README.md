# # Kantine_API

Dette er en demo-versjon av API for kafeene på UiS (Optimisten, Sentralen og Humanisten) som gir eksempeldata om kafeer, menyer, priser og vegetarretter. Det er bygget opp med Python og FastAPI.

1. `git clone https://github.com/r-akishan/Prosjekter.git`
2. Gå inn i mappen: `cd Prosjekter`
3. Lag og aktiver et virtuelt miljø.

- Lag miljøet: `python3 -m venv .venv`
- Aktiver det: 
  - Mac: `source .venv/bin/activate` 
  - Windows: `.venv\Scripts\activate`

1. Installer FastAPI: `pip install "fastapi[standard]"`
2. Gå inn i mappen: `cd Kantine-API`
3. Start serveren: `fastapi dev Kantine_API.py`
4. Åpne `http://127.0.0.1:8000/docs` i nettleseren.

**| Adresser | Hva den gjør |**

|---|---|

| `/kafeer` | alle kafeene |

| `/kafeer/{kafe_id}` | én kafe, 404 hvis den ikke finnes| 

| `/kafeer/{kafe_id}/vegetar` | vegetarretter for en kafe |

| `/kafeer/{maks_pris}/pris` | retter til en gitt pris eller lavere  |

| `/kafeer/{kafe_id}/meny` | meny for en kafe  |

**Filene i prosjektet:**

- Kantine_kode.py --> Data og funksjoner
- Kantine_API.py --> Endepunktene

