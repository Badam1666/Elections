
import streamlit as st
import time
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)

def main():
    st.title("Bienvenue sur le site de Nostradamus")
    st.subheader("Les élections européennes à votre portée")

    # Explication des élections européennes
    st.write("Nous sommes des étudiants en Data Analyse à Le Wagon. Pendant 2 semaines, nous avons analysé des données de data.gouv.fr sur les élections européennes. Notre objectif ? Sensibiliser sur l'importance des élections européennes, présenter les tendances de vote en France et proposer des prédictions pour les élections de juin 2024.")
    
    st.write("En effet, les prochaines élections européennes auront lieu du 6 au 9 juin 2024. Vous ne savez pas trop comment ces élections fonctionnent et quels sont leurs enjeux ? Pas d'inquiétude, la team Nostradamus vous aide à y voir plus clair !")
    st.write("- Tous les cinq ans, les citoyens des États membres de l'Union européenne votent pour élire leurs représentants au Parlement européen.")
    st.write("- Chaque État membre a un nombre de sièges proportionnel à sa population.")
    st.write("- Les résultats des élections européennes impactent directement le quotidien des citoyens de l'Union européenne. C'est grâce au Parlement européen que des décisions cruciales pour notre environnement ont été prises, telles que l'interdiction des plastiques à usage unique. De même, le règlement général sur la protection des données (RGPD), adopté par le Parlement européen, renforce nos droits fondamentaux à la vie privée et à la sécurité des données dans un monde de plus en plus numérisé.")
    st.write("Chaque vote aux élections européennes compte pour façonner un avenir plus durable, juste et sûr pour tous les citoyens européens !")
    st.write("Vérifiez votre inscription sur les listes électorales dans la barre latérale.")

    # Box bleue avec lien pour vérifier le statut électoral
    st.sidebar.markdown("<div style='background-color: #4169E1; padding: 8px; border-radius: 5px; margin-bottom: 10px;'>"
                        "<a style='color: white; text-decoration: none;' href='https://www.service-public.fr/particuliers/vosdroits/demarches-et-outils/ISE'>Vérifiez votre statut électoral !</a>"
                        "</div>", unsafe_allow_html=True)
    
    # Box jaune avec countdown
    st.sidebar.markdown("<div style='background-color: #FFD700; padding: 8px; border-radius: 5px;'>"
                        "<div style='color: black; font-size: small;'>"
                        "<h3>Temps restant avant la fin des inscriptions en ligne :</h3>"
                        "</div>"
                        "</div>", unsafe_allow_html=True)

    # Sur ce site
    st.subheader("Sur ce site")
    st.write("Bienvenue sur le site de Nostradamus, votre source d'informations essentielles sur les élections européennes. Sur notre plateforme, vous trouverez :")
    st.write("1. [**Classification**](https://elections-europe.streamlit.app/Classification) : Découvrez la répartition des partis politiques par orientation politique pour simplifier la compréhension et les prédictions des élections européennes.")
    st.write("2. [**Carte des Résultats**](https://elections-europe.streamlit.app/Carte_des_r%C3%A9sultats) : Explorez une carte interactive des résultats des élections européennes par département afin de visualiser les tendances politiques à travers la France depuis 2004.")
    st.write("3. [**Résultats par Commune**](https://elections-europe.streamlit.app/R%C3%A9sultats_par_commune) : Consultez les résultats des élections européennes de 2014 et 2019 dans votre commune, vous donnant un aperçu détaillé de la participation et des votes pour chaque orientation politique.")
    st.write("4. [**Prédictions**](https://elections-europe.streamlit.app/Pr%C3%A9dictions) : Accédez à nos prévisions pour les élections européennes de 2024.")
    st.write("5. [**Présentation**](https://elections-europe.streamlit.app/Pr%C3%A9sentation) : Découvrez notre analyse détaillée sur les élections européennes, incluant des clés de compréhension sur les comportements de vote")
    st.write("Notre objectif est de rendre les élections européennes accessibles à tous, afin que chacun puisse prendre des décisions éclairées et participer pleinement à la démocratie européenne.")

    
    # Countdown jusqu'au 1er Mai à minuit
    target_datetime = datetime(datetime.now().year, 5, 1, 0, 0)

    countdown_placeholder = st.sidebar.empty()

    while datetime.now() < target_datetime:
        remaining_time = target_datetime - datetime.now()
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_remaining = f"{days} jours, {hours} heures, {minutes} minutes, {seconds} secondes"
        
        countdown_placeholder.markdown("<div style='background-color: #FFD700; padding: 8px; border-radius: 5px;'>"
                                       "<div style='color: black; font-size: small;'>"
                                       f"<p>{time_remaining}</p>"
                                       "</div>"
                                       "</div>", unsafe_allow_html=True)
        
        time.sleep(1)

if __name__ == '__main__':
    main()
