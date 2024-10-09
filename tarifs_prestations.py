def get_tarifs():
    return {
        "tarif_horaire_standard": 250,  # Taux horaire moyen
        "tarif_externalisation": 150,  # Taux horaire moyen
        "facteur_urgence": 1.5,  # Facteur multiplicateur pour les cas urgents
        "droit_civil_contrats": {
            "redaction_conditions_generales": {
                "label": "Rédaction des conditions générales",
                "tarif": 800,
                "definition": "Élaboration des termes et conditions régissant les relations entre une entreprise et ses clients."
            },
            "redaction_contrat_mise_disposition_prestations_services_associes": {
                "label": "Rédaction de contrat de mise à disposition avec prestations de services associées",
                "tarif": 1500,
                "definition": "Préparation d'un contrat détaillant la mise à disposition de ressources et les services associés."
            },
            "consultation_initiale": {
                "label": "Consultation initiale",
                "tarif": 100,
                "definition": "Premier rendez-vous pour évaluer la situation juridique et définir les actions à entreprendre."
            },
            "consultation_juridique_et_reglementaire": {
                "label": "Consultation juridique et réglementaire",
                "tarif": 800,
                "definition": "Analyse approfondie d'une situation juridique spécifique et conseil sur les implications réglementaires."
            },
            "creation_entreprise": {
                "label": "Création d'entreprise",
                "tarif": 3000,
                "definition": "Accompagnement juridique complet pour la création d'une nouvelle entreprise."
            },
            "redaction_contrat_simple": {
                "label": "Rédaction de contrat simple",
                "tarif": 800,
                "definition": "Élaboration d'un contrat standard couvrant les aspects essentiels d'un accord."
            },
            "redaction_contrat_complexe": {
                "label": "Rédaction de contrat complexe",
                "tarif": 2000,
                "definition": "Préparation d'un contrat détaillé couvrant des situations juridiques complexes ou multiples."
            },
            "procedure_divorce_amiable": {
                "label": "Procédure de divorce amiable",
                "tarif": 3750,
                "definition": "Gestion juridique d'un divorce par consentement mutuel, incluant la rédaction de la convention."
            },
            "redaction_statuts_societe": {
                "label": "Rédaction des statuts de société",
                "tarif": 1200,
                "definition": "Élaboration du document juridique fondamental définissant la structure et le fonctionnement d'une société."
            },
            "depot_marque": {
                "label": "Dépôt de marque",
                "tarif": 1000,
                "definition": "Procédure juridique pour protéger une marque commerciale auprès des autorités compétentes."
            }
        },
        "droit_immobilier_commercial": {
            "redaction_bail_commercial": {
                "label": "Rédaction de bail commercial",
                "tarif": 1500,
                "definition": "Préparation d'un contrat de location pour un bien immobilier à usage commercial."
            },
            "redaction_bail_commercial_en_etat_futur_achevement_BEFA": {
                "label": "Rédaction de bail commercial en état futur d'achèvement (BEFA)",
                "tarif": 2500,
                "definition": "Élaboration d'un bail pour un local commercial encore en construction ou en rénovation."
            },
            # ... (autres prestations du droit immobilier commercial)
        },
        "droit_procedures_collectives": {
            "redaction_declaration_creance": {
                "label": "Rédaction de déclaration de créance",
                "tarif": 500,
                "definition": "Préparation du document officiel pour réclamer une dette dans le cadre d'une procédure collective."
            },
            # ... (autres prestations du droit des procédures collectives)
        },
        "contentieux_des_affaires": {
            "redaction_mise_en_demeure": {
                "label": "Rédaction de mise en demeure",
                "tarif": 300,
                "definition": "Préparation d'un courrier formel exigeant l'exécution d'une obligation ou le paiement d'une dette."
            },
            # ... (autres prestations du contentieux des affaires)
        },
        "droit_des_affaires": {
            "cession_fonds_commerce": {
                "label": "Cession de fonds de commerce",
                "tarif": 2500,
                "definition": "Accompagnement juridique pour la vente d'un fonds de commerce, incluant la rédaction des actes."
            }
        },
        "droit_construction": {
            "litige_droit_construction": {
                "label": "Litige en droit de la construction",
                "tarif": 500,
                "definition": "Gestion juridique des conflits liés aux travaux de construction ou obtenir la réparation de dommages sur un bien immobilier, telle qu'une maison ou un appartement."
            },
            # ... (autres prestations du droit de la construction)
        },
        "mediation": {
            "accompagnement_reunion_mediation": {
                "label": "Accompagnement en réunion de médiation",
                "tarif": 500,
                "definition": "Assistance et conseil lors d'une séance de médiation pour résoudre un conflit à l'amiable."
            }
        },
        "droit_societes": {
            "creation_societe_associe_unique": {
                "label": "Création de société à associé unique",
                "tarif": 600,
                "definition": "Accompagnement juridique pour la création d'une entreprise avec un seul associé (EURL, SASU)."
            },
            # ... (autres prestations du droit des sociétés)
        }
    }
