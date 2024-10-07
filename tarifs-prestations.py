# tarifs_prestations.py

TARIFS = {
    "consultation_initiale": {
        "description": "Première consultation pour évaluation du dossier",
        "prix": 150,
        "unite": "euros/heure"
    },
    "redaction_contrat": {
        "description": "Rédaction d'un contrat standard",
        "prix": 500,
        "unite": "euros/contrat"
    },
    "representation_tribunal": {
        "description": "Représentation devant le tribunal",
        "prix": 1200,
        "unite": "euros/jour"
    },
    "negociation": {
        "description": "Négociation avec la partie adverse",
        "prix": 200,
        "unite": "euros/heure"
    },
    "conseil_juridique": {
        "description": "Conseil juridique général",
        "prix": 180,
        "unite": "euros/heure"
    },
    "revision_documents": {
        "description": "Révision de documents juridiques",
        "prix": 120,
        "unite": "euros/heure"
    }
}

def get_tarifs():
    return TARIFS

def get_tarif(prestation):
    return TARIFS.get(prestation, None)
