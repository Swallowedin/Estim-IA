# prestations_heures.py

PRESTATIONS = {
    "droit_des_affaires": {
        "creation_entreprise": 10,
        "fusion_acquisition": 50,
        "redaction_contrats_commerciaux": 15,
        "litige_commercial": 30
    },
    "droit_immobilier": {
        "transaction_immobiliere": 20,
        "bail_commercial": 12,
        "litige_copropriete": 25,
        "expropriation": 40
    },
    "droit_du_travail": {
        "redaction_contrat_travail": 5,
        "licenciement": 15,
        "negociation_depart": 10,
        "litige_prudhommes": 30
    },
    "droit_de_la_famille": {
        "divorce": 40,
        "adoption": 30,
        "succession": 25,
        "pension_alimentaire": 10
    },
    "droit_penal": {
        "defense_penale": 50,
        "constitution_partie_civile": 20,
        "appel_penal": 30
    },
    "propriete_intellectuelle": {
        "depot_marque": 8,
        "litige_contrefacon": 40,
        "redaction_contrat_licence": 15
    }
}

def get_prestations():
    return PRESTATIONS

def get_heures_estimees(domaine, prestation):
    return PRESTATIONS.get(domaine, {}).get(prestation, None)
