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
instructions_module = load_py_module('./chatbot-instructions.py', 'chatbot_instructions')

# Initialisation des variables globales
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

def analyze_question(question: str, client_type: str, urgency: str) -> Tuple[str, float, bool]:
    prestations = [prestation for prestation, tarif in tarifs.items() if isinstance(tarif, (int, float))]
    prompt = f"""Analysez la question suivante et déterminez si elle est susceptible de concerner une thématique juridique. Si c'est fort probable, identifiez la prestation la plus pertinente.

Question : {question}
Type de client : {client_type}
Degré d'urgence : {urgency}

Options de prestations :
{', '.join(prestations)}
"""

    responses = get_openai_response(prompt)
    
    results = []
    for response in responses:
        try:
            lines = response.strip().split('\n')
            if len(lines) >= 2:
                results.append(lines[1])  # On prend la deuxième ligne qui devrait être la prestation
        except Exception as e:
            logger.error(f"Erreur dans l'analyse de la réponse: {e}")
    
    if not results:
        return "", 0.0, False

    prestation = max(set(results), key=results.count)
    confidence = results.count(prestation) / len(results)
    is_relevant = prestation in tarifs and isinstance(tarifs[prestation], (int, float))
    
    return prestation, confidence, is_relevant

def calculate_estimate(prestation: str, urgency: str) -> int:
    try:
        estimation = tarifs.get(prestation)
        if estimation is None:
            logger.error(f"Tarif non trouvé pour la prestation : {prestation}")
            return 0
        
        if urgency == "Urgent" and "facteur_urgence" in tarifs:
            estimation *= tarifs["facteur_urgence"]
        
        return round(estimation)
    except Exception as e:
        logger.error(f"Erreur dans calculate_estimate: {str(e)}")
        return 0

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
        if not question:
            st.warning("Veuillez décrire votre cas avant de demander une estimation.")
            return

        try:
            loading_placeholder = st.empty()
            with loading_placeholder:
                display_loading_animation()
            
            # Effectuer l'analyse
            prestation, confidence, is_relevant = analyze_question(question, client_type, urgency)

            # Supprimer l'animation de chargement
            loading_placeholder.empty()

            # Afficher les résultats de l'analyse
            st.success("Analyse terminée. Voici les résultats :")
            
            st.subheader("Indice de confiance de l'analyse")
            st.progress(confidence)
            st.write(f"Confiance : {confidence:.2%}")

            if confidence < 0.5:
                st.warning("⚠️ Attention : Notre IA a eu des difficultés à analyser votre question avec certitude. L'estimation suivante peut manquer de précision.")
            
            if not is_relevant:
                st.info("Nous ne sommes pas sûr qu'il s'agisse d'une question d'ordre juridique. L'estimation suivante est purement indicative.")

            # Afficher les détails de la prestation et l'estimation
            if prestation and prestation in tarifs:
                st.subheader("Détails de la prestation")
                st.write(f"**Prestation identifiée :** {prestation.replace('_', ' ').capitalize()}")
                
                base_tarif = tarifs[prestation]
                st.write(f"**Tarif de base :** {base_tarif} €HT")
                
                estimation = calculate_estimate(prestation, urgency)
                
                if urgency == "Urgent":
                    facteur_urgence = tarifs.get("facteur_urgence", 1.5)
                    st.write(f"**Facteur d'urgence appliqué :** x{facteur_urgence}")

                with st.container():
                    st.markdown(
                        f"""
                        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">
                            <h3 style="color: #1f618d;">Estimation finale</h3>
                            <p style="font-size: 24px; font-weight: bold; color: #2c3e50;">
                                {estimation} €HT
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.warning("Nous n'avons pas pu identifier une prestation correspondante ou calculer une estimation précise.")

            st.markdown("---")
            st.markdown("### 💡 Alternative Recommandée")
            st.info("**Consultation initiale d'une heure** - Tarif fixe : 100 € HT")

        except Exception as e:
            st.error(f"Une erreur s'est produite lors de l'analyse : {str(e)}")
            logger.exception("Erreur dans le processus d'estimation")

    st.markdown("---")
    st.write("© 2024 View Avocats. Tous droits réservés.")

if __name__ == "__main__":
    main()
