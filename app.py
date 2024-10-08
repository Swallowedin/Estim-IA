import streamlit as st
import os
from openai import OpenAI
import json
import logging
from typing import Tuple, Dict, Any
import importlib.util

st.set_page_config(page_title="View Avocats - Obtenez une estimation grâce à l'IA", page_icon="⚖️", layout="wide")

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

tarifs_module = load_py_module('./tarifs-prestations.py', 'tarifs_prestations')

# Initialisation des variables globales
tarifs = tarifs_module.get_tarifs() if tarifs_module else {}

def print_tarifs_structure():
    print("Structure de tarifs:")
    for key, value in tarifs.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")

def analyze_question(question: str, client_type: str, urgency: str) -> Tuple[str, float, bool]:
    forfaits = tarifs.get("forfaits", {})
    question_lower = question.lower()
    
    for prestation, tarif in forfaits.items():
        if prestation.lower().replace("_", " ") in question_lower:
            return prestation, 1.0, True
    
    return "Non déterminée", 0.0, False

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
        </style>
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
