import streamlit as st
import os
from openai import OpenAI
import json
import logging
from typing import Tuple, Dict, Any
import importlib.util

st.set_page_config(page_title="View Avocats - Obtenez une estimation grâce à l'IA", page_icon="⚖️", layout="wide")

# Fonction pour appliquer le CSS personnalisé
def apply_custom_css():
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp > header {
                background-color: transparent;
            }
            .stApp {
                margin-top: -80px;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            .loading-icon {
                animation: spin 1s linear infinite;
                display: inline-block;
                margin-right: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration du client OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY n'est pas défini dans les variables d'environnement")

client = OpenAI(api_key=OPENAI_API_KEY)

# Chargement des modules
def load_py_module(file_path: str, module_name: str):
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        logger.error(f"Erreur lors du chargement du module {module_name}: {e}")
        return None

prestations_module = load_py_module('./prestations-heures.py', 'prestations_heures')
tarifs_module = load_py_module('./tarifs-prestations.py', 'tarifs_prestations')
instructions_module = load_py_module('./chatbot-instructions.py', 'consignes_chatbot')

# Initialisation des variables globales
prestations = prestations_module.get_prestations() if prestations_module else {}
tarifs = tarifs_module.get_tarifs() if tarifs_module else {}
instructions = instructions_module.get_chatbot_instructions() if instructions_module else ""

def get_openai_response(prompt: str, model: str = "gpt-3.5-turbo", num_iterations: int = 3) -> list:
    try:
        responses = []
        for _ in range(num_iterations):
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": instructions},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=4000
            )
            content = response.choices[0].message.content.strip()
            responses.append(content)
        return responses
    except Exception as e:
        logger.error(f"Erreur lors de l'appel à l'API OpenAI: {e}")
        raise

import re

def analyze_question(question: str, client_type: str, urgency: str) -> Tuple[str, float, bool]:
    forfaits = tarifs.get("forfaits", {})
    
    # Définir des mots-clés pour chaque prestation
    keywords = {
        "consultation_initiale": ["consultation", "premier rendez-vous", "avis initial"],
        "création_entreprise": ["créer entreprise", "création société", "monter une affaire"],
        "rédaction_contrat_simple": ["contrat simple", "accord basique"],
        "rédaction_contrat_complexe": ["contrat complexe", "accord détaillé"],
        "procédure_divorce_amiable": ["divorce amiable", "séparation à l'amiable"],
        "rédaction_statuts_société": ["statuts société", "statuts entreprise"],
        "dépôt_marque": ["déposer marque", "enregistrement marque"],
        "rédaction_bail_commercial": ["bail commercial", "location commerce"],
        "rédaction_bail_locatif": ["bail locatif", "contrat location"],
        "assignation_justice": ["assignation", "convocation tribunal"],
        "constitution_partie_civile": ["partie civile", "se constituer partie"],
        "litige_droit_construction": ["litige construction", "conflit chantier"],
        "rédaction_contrat_construction": ["contrat construction", "accord travaux"],
        "litige_malfacons_simple": ["malfaçons simples", "défauts mineurs"],
        "litige_malfacons_complexe": ["malfaçons complexes", "vices cachés graves"],
        "assistance_expertise_judiciaire": ["expertise judiciaire", "expert tribunal"],
        "procédure_référé_construction": ["référé construction", "urgence chantier"]
    }
    
    # Fonction pour trouver la meilleure correspondance
    def find_best_match(text):
        best_match = None
        max_count = 0
        for prestation, kw_list in keywords.items():
            count = sum(1 for kw in kw_list if re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE))
            if count > max_count:
                max_count = count
                best_match = prestation
        return best_match, max_count

    # Trouver la meilleure correspondance
    service, keyword_count = find_best_match(question.lower())
    
    # Calculer la confiance basée sur le nombre de mots-clés trouvés
    confidence = min(keyword_count / 2, 1.0)  # 2 mots-clés ou plus donnent une confiance de 100%
    
    # Vérifier si le service est dans les forfaits
    is_relevant = service in forfaits
    
    if not is_relevant:
        service = "Non déterminée"
        confidence = 0.0

    return service, confidence, is_relevant
    
def calculate_estimate(domaine: str, prestation: str, urgency: str) -> int:
    try:
        # Chercher d'abord dans les forfaits
        forfait = tarifs.get("forfaits", {}).get(domaine, {}).get(prestation, {}).get("tarif")
        
        # Si pas de forfait, calculer basé sur les heures
        if forfait is None:
            heures = prestations.get(domaine, {}).get(prestation, 10)
            tarif_horaire = tarifs.get("tarif_horaire_standard", 250)
            estimation = heures * tarif_horaire
        else:
            estimation = forfait

        # Appliquer le facteur d'urgence si nécessaire
        if urgency == "Urgent":
            facteur_urgence = tarifs.get("facteur_urgence", 1.5)
            estimation *= facteur_urgence

        return round(estimation)
    except Exception as e:
        logger.exception(f"Erreur dans calculate_estimate: {str(e)}")
        raise

def display_loading_animation():
    return st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center; flex-direction: column;">
        <svg class="loading-icon" width="50" height="50" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,1,1,1,8-8A8,8,0,0,1,12,20Z" opacity=".25"/>
            <path d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z"/>
        </svg>
        <p style="margin-top: 10px; font-weight: bold;">Estim'IA analyse votre cas juridique...</p>
        <p>Veuillez patienter quelques secondes !</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    apply_custom_css()
    
    st.title("🏛️ View Avocats - Estim'IA")

    client_type = st.selectbox("Vous êtes :", ("Particulier", "Entreprise"))
    urgency = st.selectbox("Degré d'urgence :", ("Normal", "Urgent"))
    question = st.text_area("Expliquez brièvement votre cas, notre intelligence artificielle s'occupe du reste !", height=150)

    if st.button("Obtenir une estimation grâce à l'intelligence artificielle"):
        if question:
            try:
                # Afficher la structure de tarifs pour le débogage
                print_tarifs_structure()
                
                # Effectuer l'analyse et le calcul
                service, confidence, is_relevant = analyze_question(question, client_type, urgency)
                
                estimation = tarifs["forfaits"].get(service) if is_relevant else None
                if estimation and urgency == "Urgent":
                    estimation *= tarifs["facteur_urgence"]

                # Afficher les résultats
                st.success("Analyse terminée. Voici les résultats :")
                
                if service == "Non déterminée":
                    st.warning("⚠️ Nous n'avons pas pu identifier précisément votre besoin. Voici la liste des prestations disponibles :")
                    for prestation in tarifs["forfaits"].keys():
                        st.write(f"- {prestation.replace('_', ' ').capitalize()}")
                else:
                    st.subheader("Résumé de l'estimation")
                    st.write(f"**Prestation identifiée :** {service.replace('_', ' ').capitalize()}")

                    if estimation:
                        st.markdown(
                            f"""
                            <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">
                                <h3 style="color: #1f618d;">Estimation</h3>
                                <p style="font-size: 24px; font-weight: bold; color: #2c3e50;">
                                    À partir de {round(estimation)} €HT
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                st.markdown("---")
                st.markdown("### 💡 Alternative Recommandée")
                st.info("**Consultation initiale d'une heure** - Tarif fixe : 100 € HT")

            except Exception as e:
                st.error(f"Une erreur s'est produite : {str(e)}")
                logger.exception("Erreur dans le processus d'estimation")
        else:
            st.warning("Veuillez décrire votre cas avant de demander une estimation.")

    st.markdown("---")
    st.write("© 2024 View Avocats. Tous droits réservés.")

if __name__ == "__main__":
    main()
