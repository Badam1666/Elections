import streamlit as st
import time
from datetime import datetime, timedelta

def main():
    st.title("Bienvenue sur le site de Nostradamus")
    st.subheader("Les élections européennes à votre portée")

    # Explication des élections européennes
    st.write("Les élections européennes sont un moment crucial où vous pouvez exercer votre droit de vote "
             "et influencer l'avenir de l'Union européenne. C'est votre opportunité de faire entendre votre voix "
             "et de participer à la démocratie européenne.")

    # Box bleue avec lien pour vérifier le statut électoral
    st.sidebar.markdown("<div style='background-color: #87CEEB; padding: 10px; border-radius: 5px;'>"
                        "<a style='color: white; text-decoration: none;' href='https://www.service-public.fr/particuliers/vosdroits/demarches-et-outils/ISE'>Vérifiez votre statut électoral !</a>"
                        "</div>", unsafe_allow_html=True)

 
    # Description du site
    st.header("À propos de Nostradamus")
    st.write("Nostradamus est votre source de prévisions électorales, vous aidant à comprendre les tendances "
             "et les enjeux des élections européennes. Nous mettons à votre disposition des analyses approfondies, des "
             "données en temps réel et des outils interactifs pour vous permettre de prendre des décisions éclairées.")

    # Nos prévisions
    st.header("Nos Prévisions")
    st.write("Nos experts prévoient une participation record pour les prochaines élections européennes. "
             "Nous prévoyons également des changements significatifs dans la composition du Parlement européen, avec "
             "des implications majeures pour l'avenir de l'Union européenne.")

    # Countdown jusqu'au 1er Mai à minuit
    target_datetime = datetime(datetime.now().year, 5, 1, 0, 0)

    countdown_placeholder = st.sidebar.empty()

    while datetime.now() < target_datetime:
        remaining_time = target_datetime - datetime.now()
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_remaining = f"{days} jours, {hours} heures, {minutes} minutes, {seconds} secondes"
        
        countdown_placeholder.markdown(f"<h3>Temps restant avant la fin des inscriptions en ligne : {time_remaining}</h3>", unsafe_allow_html=True)
        
        time.sleep(1)

if __name__ == '__main__':
    main()
