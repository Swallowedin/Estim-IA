def get_tarifs():
    return {
        "tarif_horaire_standard": 250,  # Taux horaire moyen
        "tarif_externalisation": 150,  # Taux horaire moyen
        "facteur_urgence": 1.5,  # Facteur multiplicateur pour les cas urgents
        "forfaits": {
            "droit_civil_contrats": {
                "Rédaction_conditions_générales": 800,
                "Rédaction_contrat_mise_disposition_prestations_services_associés": 1500,
                "consultation_initiale": 100,
                "consultation_juridique_et_reglementaire": 800,
                "création_entreprise": 3000,
                "rédaction_contrat_simple": 800,
                "rédaction_contrat_complexe": 2000,
                "procédure_divorce_amiable": 3750,
                "rédaction_statuts_société": 1200,
                "dépôt_marque": 1000
                },
            "droit_immobilier_commercial": {
                "rédaction_bail_commercial": 1500,
                "rédaction_bail_commercial_en_etat_futur_achevement_BEFA": 2500,
                "rédaction_bail_commercial_dérogatoire": 1000,
                "rédaction_bail_sous_location": 1000,
                "rédaction_bail_professionnel": 800,
                "rédaction_avenant_bail_commercial": 500,
                "rédaction_demande_révision_loyer": 500,
                "rédaction_demande_déspécialisation": 400,
                "Procédure_résiliation_bail_commercial": 1500,
                "Rédaction_commandement_clause_résolutoire": 400,
                "Mise_en_demeure_conflit_bail_commercial": 400,
                "Procédure_recouvrement_impayés": 500,
                "Rédaction_congé": 400,
                "Rédaction_demande_renouvellement": 400,
                "Rédaction_mémoire_fixation_loyer_bail_renouvelé": 1000,
                "Procédure_juge_loyers_commerciaux": 3000,
                "Purge_droit_préemption": 500,
                "Rédaction_cession_droit_bail": 1500,
                "Procédure_bail_commercial_tribunal_judiciaire_fond": 2000,
                "Procédure_fixation_indemnité_éviction": 4000
                },
            "droit_procédures_collectives": {
                "rédaction_déclaration_créance": 500,
                "contestation_créance_juge_commissaire": 1000,
                "Déclaration_cessation_paiements": 800,
                "Accompagnement_audience": 400,
                "Rédaction_offre_reprise": 2000,
                "Défense_sanction_personnelle_dirigeant": 1500
                },
            "contentieux_des_affaires": {
                "rédaction_mise_en_demeure": 300,
                "requete_injonction_payer": 600,
                "négociation_redaction_protocole_accord_transactionnel": 1000,
                "Procédure_fond_tribunal_commerce": 2000,
                "Procédure_fond_tribunal_judiciaire": 2000,
                "Procédure_référé_provision": 1000,
                "Procédure_référé_expertise": 800,
                "Suivi_Expertise_judiciaire": 1000,
                "Procédure_appel": 2000,
                "Demande_ouverture_procédure_redressement_ou_liquidation": 1000
                },
            "Droit_des_affaires": {
                "Cession_fonds_commerce": 2500
            },
            
            "droit_construction": {
                "litige_droit_construction": 500,
                "rédaction_contrat_construction": 2500,
                "litige_malfacons_simple": 5000,
                "litige_malfacons_complexe": 10000,
                "assistance_expertise_judiciaire": 2000,
                "procédure_référé_construction": 3750
                },
            "Médiation": {
                "Accompagnement_réunion_médiation": 500
            },
            "Droit_sociétés": {
                "Création_société_associé_unique": 600,
                "Création_sa_sas_sarl": 750,
                "Création_société_exercice_libéral_associé_unique": 1200,
                "Création_société_exercice_libérale": 1500
            },
            "frais_additionnels": {
                "frais_de_dossier": 150,
                "frais_de_déplacement_par_km": 0.6,
                "forfait_expertise_judiciaire": 1000,
                "forfait_déplacement_chantier": 300
            },
        }
    }
