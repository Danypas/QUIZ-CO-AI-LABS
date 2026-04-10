import streamlit as st

# Configuration de la page
st.title("Mon premier Quiz IA Offline")

questions = {
    "L'IA Offline nécessite-t-elle une connexion Cloud ? (oui/non)": "non",
    "Le format JSON est-il utilisé pour structurer les données ? (oui/non)": "oui",
    "Un SLM est-il plus lourd qu'un LLM classique ? (oui/non)": "non"
}

score = 0

st.write("--- DÉBUT DE L'ÉVALUATION DES ACQUIS ---")

# Utilisation d'un formulaire pour éviter que la page ne saute à chaque réponse
with st.form("quiz_form"):
    reponses_finales = {}
    
    for q in questions.keys():
        # On crée un champ de saisie pour chaque question
        reponses_finales[q] = st.text_input(q)
    
    # Bouton de validation
    submitted = st.form_submit_button("Valider mes réponses")

if submitted:
    for q, reponse_attendue in questions.items():
        reponse_u = reponses_finales[q].lower().strip()
        
        if reponse_u == reponse_attendue:
            st.success(f"✅ {q} : Correct !")
            score += 1
        else:
            st.error(f"❌ {q} : Erreur... La bonne réponse était : {reponse_attendue}")

    st.subheader(f"SCORE FINAL : {score}/{len(questions)}")
    
    if score == len(questions):
        st.balloons() # Un petit effet visuel pour la réussite !
        st.info("Félicitations, objectif pédagogique atteint !")