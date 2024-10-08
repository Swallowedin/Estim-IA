def get_tarifs():
    return {
        "tarif_horaire_standard": 250,  # Taux horaire moyen
        "tarif_externalisation": 150,  # Taux horaire moyen
        "facteur_urgence": 1.5,  # Facteur multiplicateur pour les cas urgents
        "forfaits": {
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
                "redaction_bail_commercial_derogatoire": {
                    "label": "Rédaction de bail commercial dérogatoire",
                    "tarif": 1000,
                    "definition": "Préparation d'un bail commercial de courte durée, dérogeant au statut des baux commerciaux."
                },
                "redaction_bail_sous_location": {
                    "label": "Rédaction de bail de sous-location",
                    "tarif": 1000,
                    "definition": "Élaboration d'un contrat permettant à un locataire de louer tout ou partie du bien à un tiers."
                },
                "redaction_bail_professionnel": {
                    "label": "Rédaction de bail professionnel",
                    "tarif": 800,
                    "definition": "Préparation d'un contrat de location pour un local destiné à l'exercice d'une profession libérale."
                },
                "redaction_avenant_bail_commercial": {
                    "label": "Rédaction d'avenant à bail commercial",
                    "tarif": 500,
                    "definition": "Élaboration d'un document modifiant les termes d'un bail commercial existant."
                },
                "redaction_demande_revision_loyer": {
                    "label": "Rédaction de demande de révision de loyer",
                    "tarif": 500,
                    "definition": "Préparation d'une requête formelle pour ajuster le montant du loyer d'un bail commercial."
                },
                "redaction_demande_despecialisation": {
                    "label": "Rédaction de demande de déspécialisation",
                    "tarif": 400,
                    "definition": "Élaboration d'une demande pour modifier l'activité autorisée ou la destination dans un bail commercial."
                },
                "procedure_resiliation_bail_commercial": {
                    "label": "Procédure de résiliation de bail commercial",
                    "tarif": 1500,
                    "definition": "Gestion juridique de la fin anticipée d'un bail commercial."
                },
                "redaction_commandement_clause_resolutoire": {
                    "label": "Rédaction de commandement visant la clause résolutoire",
                    "tarif": 400,
                    "definition": "Préparation d'un acte formel mettant en œuvre la clause de résiliation automatique du bail."
                },
                "mise_en_demeure_conflit_bail_commercial": {
                    "label": "Mise en demeure pour conflit de bail commercial",
                    "tarif": 400,
                    "definition": "Rédaction d'un avertissement formel dans le cadre d'un litige lié à un bail commercial."
                },
                "procedure_recouvrement_impayes": {
                    "label": "Procédure de recouvrement d'impayés",
                    "tarif": 500,
                    "definition": "Gestion juridique pour récupérer des loyers ou charges impayés dans le cadre d'un bail commercial."
                },
                "redaction_conge": {
                    "label": "Rédaction de congé",
                    "tarif": 400,
                    "definition": "Préparation de l'acte mettant fin à un bail commercial à son terme."
                },
                "redaction_demande_renouvellement": {
                    "label": "Rédaction de demande de renouvellement",
                    "tarif": 400,
                    "definition": "Élaboration d'une requête formelle pour prolonger un bail commercial arrivant à échéance."
                },
                "redaction_memoire_fixation_loyer_bail_renouvele": {
                    "label": "Rédaction de mémoire pour la fixation du loyer de bail renouvelé",
                    "tarif": 1000,
                    "definition": "Préparation d'un document argumenté pour déterminer le nouveau loyer lors du renouvellement d'un bail."
                },
                "procedure_juge_loyers_commerciaux": {
                    "label": "Procédure devant le juge des loyers commerciaux",
                    "tarif": 3000,
                    "definition": "Représentation juridique dans un litige concernant le loyer d'un bail commercial."
                },
                "purge_droit_preemption": {
                    "label": "Purge du droit de préemption",
                    "tarif": 500,
                    "definition": "Procédure visant à s'assurer qu'aucun tiers n'a de droit prioritaire d'achat sur un bien commercial."
                },
                "redaction_cession_droit_bail": {
                    "label": "Rédaction de cession de droit au bail",
                    "tarif": 1500,
                    "definition": "Élaboration du contrat transférant les droits et obligations d'un bail commercial à un nouveau locataire."
                },
                "procedure_bail_commercial_tribunal_judiciaire_fond": {
                    "label": "Procédure de bail commercial devant le tribunal judiciaire (fond)",
                    "tarif": 2000,
                    "definition": "Représentation juridique dans un litige complexe lié à un bail commercial devant le tribunal."
                },
                "procedure_fixation_indemnite_eviction": {
                    "label": "Procédure de fixation d'indemnité d'éviction",
                    "tarif": 4000,
                    "definition": "Gestion juridique pour déterminer la compensation due au locataire en cas de non-renouvellement du bail."
                }
            },
            "droit_procedures_collectives": {
                "redaction_declaration_creance": {
                    "label": "Rédaction de déclaration de créance",
                    "tarif": 500,
                    "definition": "Préparation du document officiel pour réclamer une dette dans le cadre d'une procédure collective."
                },
                "contestation_creance_juge_commissaire": {
                    "label": "Contestation de créance devant le juge-commissaire",
                    "tarif": 1000,
                    "definition": "Procédure pour contester une créance déclarée dans une procédure collective."
                },
                "declaration_cessation_paiements": {
                    "label": "Déclaration de cessation des paiements",
                    "tarif": 800,
                    "definition": "Préparation et dépôt de la déclaration officielle d'incapacité à payer ses dettes."
                },
                "accompagnement_audience": {
                    "label": "Accompagnement en audience",
                    "tarif": 400,
                    "definition": "Assistance et représentation du client lors des audiences liées aux procédures collectives."
                },
                "redaction_offre_reprise": {
                    "label": "Rédaction d'offre de reprise",
                    "tarif": 2000,
                    "definition": "Élaboration d'une proposition pour reprendre tout ou partie d'une entreprise en difficulté."
                },
                "defense_sanction_personnelle_dirigeant": {
                    "label": "Défense contre sanction personnelle du dirigeant",
                    "tarif": 1500,
                    "definition": "Représentation juridique d'un dirigeant face à des accusations de faute de gestion."
                }
            },
            "contentieux_des_affaires": {
                "redaction_mise_en_demeure": {
                    "label": "Rédaction de mise en demeure",
                    "tarif": 300,
                    "definition": "Préparation d'un courrier formel exigeant l'exécution d'une obligation ou le paiement d'une dette."
                },
                "requete_injonction_payer": {
                    "label": "Requête en injonction de payer",
                    "tarif": 600,
                    "definition": "Procédure simplifiée pour obtenir un titre exécutoire en vue du recouvrement d'une créance."
                },
                "negociation_redaction_protocole_accord_transactionnel": {
                    "label": "Négociation et rédaction de protocole d'accord transactionnel",
                    "tarif": 1000,
                    "definition": "Élaboration d'un accord amiable pour résoudre un litige entre parties."
                },
                "procedure_fond_tribunal_commerce": {
                    "label": "Procédure au fond devant le tribunal de commerce",
                    "tarif": 2000,
                    "definition": "Représentation dans un litige commercial devant le tribunal compétent."
                },
                "procedure_fond_tribunal_judiciaire": {
                    "label": "Procédure au fond devant le tribunal judiciaire",
                    "tarif": 2000,
                    "definition": "Représentation dans un litige civil ou commercial devant le tribunal judiciaire."
                },
                "procedure_refere_provision": {
                    "label": "Procédure en référé provision",
                    "tarif": 1000,
                    "definition": "Assistance, accompagnement et représentation en justice afin d'entamer une procédure d'urgence pour obtenir le paiement provisoire d'une créance non sérieusement contestable  par un débiteur récalcitrant."
                },
                "procedure_refere_expertise": {
                    "label": "Procédure en référé expertise",
                    "tarif": 800,
                    "definition": "Assistance, accompagnement et représentation en justice afin d'entamer une procédure d'urgence pour obtenir la désignation d'un expert par le tribunal afin de déclencher une expertise qui permettra de déterminer les responsabilité de chacun dans le cadre d'un conflit."
                },
                "suivi_expertise_judiciaire": {
                    "label": "Suivi d'expertise judiciaire",
                    "tarif": 1000,
                    "definition": "Accompagnement et représentation du client durant la pahse d'expertise décidée par un tribunal."
                },
                "procedure_appel": {
                    "label": "Procédure d'appel",
                    "tarif": 2000,
                    "definition": "Représentation du client devant la cour d'appel pour contester un jugement de première instance."
                },
                "demande_ouverture_procedure_redressement_ou_liquidation": {
                    "label": "Demande d'ouverture de procédure de redressement ou liquidation",
                    "tarif": 1000,
                    "definition": "Préparation et dépôt d'une requête pour initier une procédure collective."
                }
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
                "definition": "Gestion juridique des conflits liés aux travaux de construction ou obtenir la réparartion de dommages sur un bien immobilier, telle qu'une maison ou un appartement."
            },
            "redaction_contrat_construction": {
                "label": "Rédaction de contrat de construction",
                "tarif": 2500,
                "definition": "Élaboration d'un contrat détaillant les termes et conditions d'un projet de construction d'un bien immobilier."
            },
            "litige_malfacons_simple": {
                "label": "Litige pour malfaçons simple",
                "tarif": 5000,
                "definition": "Représentation en justice dans un cas de défauts de construction ou de dommages sur un bien immobilier d'une complexité limitée."
            },
            "litige_malfacons_complexe": {
                "label": "Litige pour malfaçons complexe",
                "tarif": 10000,
                "definition": "Représentation en justice dans le cadre d'un contentieux impliquant des défauts de construction, ou des dommages, multiples ou techniques."
            },
            "assistance_expertise_judiciaire": {
                "label": "Assistance lors d'une expertise judiciaire",
                "tarif": 2000,
                "definition": "Accompagnement du client lors de la phase d'expertise décidée par un tribunal en matière de litige portant sur le domaine de la construction et de biens immobiliers."
            },
            "procedure_refere_construction": {
                "label": "Procédure en référé construction",
                "tarif": 3750,
                "definition": "Assistance, accompagnement et représentation en justice afin d'entamer une procédure d'urgence pour obtenir la désignation d'urgence d'un expert afin de déterminer les responsabilités de chacun dans le cadre d'un litige de construction."
            }
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
            "creation_sa_sas_sarl": {
                "label": "Création de SA, SAS ou SARL",
                "tarif": 750,
                "definition": "Assistance juridique complète pour la constitution d'une société anonyme, par actions simplifiée ou à responsabilité limitée."
            },
            "creation_societe_exercice_liberal_associe_unique": {
                "label": "Création de société d'exercice libéral à associé unique",
                "tarif": 1200,
                "definition": "Mise en place d'une structure juridique pour l'exercice individuel d'une profession libérale réglementée."
            },
            "creation_societe_exercice_liberale": {
                "label": "Création de société d'exercice libérale",
                "tarif": 1500,
                "definition": "Établissement d'une société pour l'exercice en commun de professions libérales réglementées."
            }
        }
    }

