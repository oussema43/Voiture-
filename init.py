from json import dump, load

def load_voitures():
    try:
        with open("voitures.json", "r") as f:
            voitures = load(f)
        print("Voitures chargées avec succès.")
        return voitures
    except FileNotFoundError:
        print("Aucune voiture trouvée. Création d'un nouveau fichier.")
        return {}
    except Exception as e:
        print(f"Erreur lors du chargement des voitures: {e}")
        return {}

def sauvegarder_voitures(voitures):
    with open("voitures.json", "w") as f:
        dump(voitures, f, indent=4)

def get_next_id(data):
    if data:
        numeric_keys = [int(k) for k in data.keys() if str(k).isdigit()]
        if numeric_keys:
            return max(numeric_keys) + 1
    return 1

def ajouter_voiture(marque, modele, annee):
    voitures = load_voitures()
    next_id = get_next_id(voitures)
    voitures[next_id] = {
        "marque": marque,
        "modele": modele,
        "annee": annee,
        "disponible": True
    }
    sauvegarder_voitures(voitures)
    return voitures

def afficher_voitures(voitures):
    print("Voitures disponibles: ")
    for id, voiture in voitures.items():
        if voiture["disponible"]:
            print(f"ID: {id}, Marque: {voiture['marque']}, Modèle: {voiture['modele']}, Année: {voiture['annee']}, Statut: Disponible")
    return voitures

def louer_voiture(voitures, id):
    id = str(id)
    if id in voitures:
        if voitures[id]["disponible"]:
            voitures[id]["disponible"] = False
            print("Voiture louée avec succès.")
        else:
            print("Désolé, cette voiture est déjà louée.")
    else:
        print("Voiture non trouvée.")
    sauvegarder_voitures(voitures)
    return voitures

def retourner_voiture(voitures, id):
    id = str(id)
    if id in voitures:
        if not voitures[id]["disponible"]:
            voitures[id]["disponible"] = True
            print("Voiture retournée avec succès.")
        else:
            print("Désolé, cette voiture est déjà disponible.")
    else:
        print("Voiture non trouvée.")
    sauvegarder_voitures(voitures)
    return voitures

def supprimer_voiture(voitures, id):
    id = str(id)
    if id in voitures:
        del voitures[id]
        print("Voiture supprimée avec succès.")
    else:
        print("Voiture non trouvée.")
    sauvegarder_voitures(voitures)
    return voitures


def quitter(voitures):
    sauvegarder_voitures(voitures)
    exit()

voitures = load_voitures()
