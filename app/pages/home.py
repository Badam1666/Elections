import streamlit as st

def show_home_page():
    st.title("Accueil")
    st.write("Bienvenue sur notre application sur les élections européennes!")
    # Add more content or Streamlit components as needed for your home page

import time
from datetime import datetime, timezone, timedelta

def count_down(target_datetime):
    with st.empty():
        while datetime.now(timezone.utc) < target_datetime:
            remaining_time = target_datetime - datetime.now(timezone.utc)
            days, seconds = divmod(remaining_time.total_seconds(), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)
            
            time_remaining = f"{int(days)} jours, {int(hours)} heures, {int(minutes)} minutes, {int(seconds)} secondes"
            
            st.title("Countdown")
            st.header(f"Temps restant : {time_remaining}")
            time.sleep(1)
        
        st.header("Fin des inscriptions en ligne")

def main():
    st.title("Bienvenue sur le site de Nostradamus")
    st.subheader("Les élections européennes à votre portée")

    target_datetime = datetime(2024, 5, 1, 0, 0, tzinfo=timezone.utc)
    count_down(target_datetime)

    st.markdown("---")
    st.write("Les élections européennes sont un moment crucial où vous pouvez exercer votre droit de vote et influencer l'avenir de l'Union européenne. C'est votre opportunité de faire entendre votre voix et de participer à la démocratie européenne.")
    st.write("Nostradamus est votre source de prévisions électorales, vous aidant à comprendre les tendances et les enjeux des élections européennes. Nous mettons à votre disposition des analyses approfondies, des données en temps réel et des outils interactifs pour vous permettre de prendre des décisions éclairées.")
    st.write("Nos experts prévoient une participation record pour les prochaines élections européennes. Nous prévoyons également des changements significatifs dans la composition du Parlement européen, avec des implications majeures pour l'avenir de l'Union européenne.")
    st.write("Rejoignez-nous pour cette expérience unique!")

if __name__ == '__main__':
    main()


