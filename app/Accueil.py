
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
    st.write("Les prochaines élections européennes auront lieu du 6 au 9 juin 2024. Vous ne savez pas trop comment ces élections fonctionnent et quels sont leurs enjeux ? Pas d'inquiétude, la team Nostradamus vous aide à y voir plus clair !")
    st.write("- Tous les cinq ans, les citoyens des États membres de l'Union européenne votent pour élire leurs représentants au Parlement européen.")
    st.write("- Chaque État membre a un nombre de sièges proportionnel à sa population.")
    st.write("- Les résultats des élections européennes impactent directement le quotidien des citoyens de l'Union européenne. C'est grâce au Parlement européen que des décisions cruciales pour notre environnement ont été prises, telles que l'interdiction des plastiques à usage unique. De même, le règlement général sur la protection des données (RGPD), adopté par le Parlement européen, renforce nos droits fondamentaux à la vie privée et à la sécurité des données dans un monde de plus en plus numérisé.")
    st.write("Vous trouverez également un lien dans la barre latérale pour vérifier votre inscription sur la liste électorale pour les élections européennes de juin, ainsi qu'un compte à rebours pour la clôture des inscriptions en ligne.")
    st.write("Chaque vote aux élections européennes compte pour façonner un avenir plus durable, juste et sûr pour tous les citoyens européens !")

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
    st.write("1. [**Carte des Résultat**](https://elections-europe.streamlit.app/Carte) : Explorez une carte interactive des résultats des élections européennes par département afin de visualiser les tendances politiques à travers la France depuis 2004.")
    st.write("2. [**Résultats par Commune**](https://elections-europe.streamlit.app/Communes) : Consultez les résultats des élections européennes de 2014 et 2019 dans votre commune, vous donnant un aperçu détaillé de la participation et des votes pour chaque parti politique.")
    st.write("3. [**Présentation**](https://elections-europe.streamlit.app/Presentation) : Consultez les résultats des élections européennes de 2014 et 2019 dans votre commune, vous donnant un aperçu détaillé de la participation et des votes pour chaque parti politique.")
    st.write("Notre objectif est de rendre les élections européennes accessibles à tous, afin que chacun puisse prendre des décisions éclairées et participer pleinement à la démocratie européenne.")

    # Répartition
    st.subheader("Répartion par orientation politique")
    
    st.write("Durant les 20 dernières annnées d'élections européennes, les noms des partis et nuances politiques ont changé considérablement. Pour pouvoir être cohérent dans nos analyses et dans nos prédictions, nous avons décidé de les classer par orientation politique. Nous avons utilisé le site internet de chacun de ces partis et les informations de l'Assemblée Nationale pour effectuer ce tri.")
    data = {
        2004: {
            'Extrême gauche': "LPC, LXG",
            'Gauche': "LPS, LDG",
            'Centre gauche': "LEC, LVE",
            'Centre': "-",
            'Centre droite': "LUDF",
            'Droite': "LUMP, LCP, LDD",
            'Extrême droite': "LFN, LXD",
            'Divers': "LDV, LRG"
        },
        2009: {
            'Extrême gauche': "LEXG, LCOP",
            'Gauche': "LSOC, LDVD",
            'Centre gauche': "LVEC",
            'Centre': "LCMD",
            'Centre droite': "-",
            'Droite': "LMAJ, LDVD",
            'Extrême droite': "LFN, LEXD",
            'Divers': "LAUT, LREG"
        },
        2014: {
            'Extrême gauche': "LEXG, LFG",
            'Gauche': "LDVG, LUG",
            'Centre gauche': "LVEC",
            'Centre': "LUC",
            'Centre droite': "-",
            'Droite': "LDVD, LUMP",
            'Extrême droite': "LFN, LEXD",
            'Divers': "LDIV"
        },
        2019: {
            'Extrême gauche': "La France Insoumise, L'Europe des gens",
            'Gauche': "Liste citoyenne",
            'Centre gauche': "Europe Ecologie, Envie d'Europe, Urgence Ecologie",
            'Centre': "Renaissance",
            'Centre droite': "Union Droite Centre, Les européens",
            'Droite': "-",
            'Extrême droite': "Prenez le pouvoir (RN), Debout ! La France, Ensemble pour le Frexit",
            'Divers': "Parti animaliste"
        },
        2024: {
            'Extrême gauche': "La France Insoumise, Lutte ouvrière, NPA, PCF",
            'Gauche': "Parti socialiste et Place Publique",
            'Centre gauche': "Europe Ecologie les Verts,Parti radical de Gauche",
            'Centre': "Renaissance, Ecologie au centre",
            'Centre droite': "Alliance rurale",
            'Droite': "Les republicains, Notre Europe",
            'Extrême droite': "Debout ! La France, Reconquête, Rassemblement national, Union populaire républicaine",
            'Divers': "Parti animaliste"
        }
    }

    df = pd.DataFrame(data)
    st.table(df)
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
