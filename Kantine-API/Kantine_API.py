from fastapi import FastAPI, HTTPException                  # Importerer et fast API
from Kantine_kode import KAFEER, hent_kafe, vegetarretter, rimelige_rett
                                                            # Setter opp et minimalt API
app = FastAPI()

@app.get("/kafeer")  # Sender get-forespørsel til kafeer
def alle_kafeer():   # Lager en funksjon som returnerer alle kafeer
    return KAFEER

@app.get("/kafeer/{kafe_id}")                                               # Sender get-forespørsel til en spesifikk kafe
def en_kafe(kafe_id):                                                       # Lager en funksjon som returnerer den spesifikke kafeen
    kafe_resturant = hent_kafe(kafe_id)
    if kafe_resturant is None:                                          
        raise HTTPException(status_code = 404, detail = "Kafé ikke funnet!")# Gir en feilmelding dersom kafeen ikke finnes
    return kafe_resturant

@app.get("/kafeer/{kafe_id}/vegetar")                                       # Sender get-forespørsel for vegetarretter
def vegetarmat(kafe_id):                                                    # Lager en funksjon som returnerer vegetarretten fra deres kafe
    kafe_vegetar = vegetarretter(kafe_id)
    kafe_resturant = hent_kafe(kafe_id)
    if kafe_resturant is None:
        raise HTTPException(status_code = 404, detail = "Kafé ikke funnet!")# Gir en feilmelding dersom kafeen ikke finnes
    elif kafe_vegetar == []:    
        return f"{kafe_id} har dessverre ingen vegetarretter idag!"         # Hvis det ikke tilbys noe vegetarretter
    return kafe_vegetar

@app.get("/kafeer/{maks_pris}/pris")                                               # Sender get-forespørsel for å finne retter til budsjettet mitt
def billig_rett(maks_pris: int):                                                   # Lager en funksjon som returnerer rettene som jeg kan kjøpe
    kafe_rimelig = rimelige_rett(maks_pris)
    if kafe_rimelig == []:
        return f"Dessverre ingen retter som når budsjettet ditt på {maks_pris}kr!" # Budsjettet er for lavt
    return kafe_rimelig