import streamlit as st

def show_home_page():
    st.title("Accueil")
    st.write("Bienvenue sur notre application sur les élections européennes!")
    # Add more content or Streamlit components as needed for your home page
import time
from datetime import datetime, timedelta

# Titre et sous-titre
st.title("Bienvenue sur le site de Nostradamus")
st.subheader("Les élections européennes à votre portée")

# Explication rapide des élections européennes
st.write("Les élections européennes sont un moment crucial où vous pouvez exercer votre droit de vote \
et influencer l'avenir de l'Union européenne. C'est votre opportunité de faire entendre votre voix \
et de participer à la démocratie européenne.")

# Image avec lien
st.sidebar.image("elections.jpg", use_column_width=True)
st.sidebar.markdown("[Vérifiez votre statut électoral !](https://www.service-public.fr/particuliers/vosdroits/demarches-et-outils/ISE)")

# Countdown
target_date = datetime(datetime.now().year, 5, 1, 0, 0)  # 1er Mai à minuit
time_left = target_date - datetime.now()

st.sidebar.title("Countdown")
st.sidebar.write(f"Il reste {time_left.days} jours et {time_left.seconds // 3600} heures avant la fin des inscriptions en ligne.")

# Description du site
st.header("À propos de Nostradamus")
st.write("Nostradamus est votre source de prévisions électorales, vous aidant à comprendre les tendances \
et les enjeux des élections européennes. Nous mettons à votre disposition des analyses approfondies, des \
données en temps réel et des outils interactifs pour vous permettre de prendre des décisions éclairées.")

# Nos prévisions
st.header("Nos Prévisions")
st.write("Nos experts prévoient une participation record pour les prochaines élections européennes. \
Nous prévoyons également des changements significatifs dans la composition du Parlement européen, avec \
des implications majeures pour l'avenir de l'Union européenne.")

# Crédits
st.write("Site développé par Nostradamus. Tous droits réservés.")

