import streamlit as st
from datetime import datetime, timedelta

def main():
    st.title("Bienvenue sur le site de Nostradamus")
    st.subheader("Les élections européennes à votre portée")

    # Explication des élections européennes
    st.write("Les prochaines élections européennes auront lieu du 6 au 9 juin 2024. Vous ne savez pas trop comment ces élections fonctionnent et quels sont leurs enjeux ? Pas d'inquiétude, la team Nostradamus vous aide à y voir plus clair !")
    st.write("- Tous les cinq ans, les citoyens des États membres de l'Union européenne votent pour élire leurs représentants au Parlement européen.")
    st.write("- Chaque État membre a un nombre de sièges proportionnel à sa population.")
    st.write("- Les résultats des élections européennes impactent directement le quotidien des citoyens de l'Union européenne. C'est grâce au Parlement européen que des décisions cruciales pour notre environnement ont été prises, telles que l'interdiction des plastiques à usage unique. De même, le règlement général sur la protection des données (RGPD), adopté par le Parlement européen, renforce nos droits fondamentaux à la vie privée et à la sécurité des données dans un monde de plus en plus numérisé.")
    st.write("Chaque vote aux élections européennes compte pour façonner un avenir plus durable, juste et sûr pour tous les citoyens européens !")

    # Box bleue avec lien pour vérifier le statut électoral
    st.sidebar.markdown("<div style='background-color: #4169E1; padding: 8px; border-radius: 5px; margin-bottom: 10px;'>"
                        "<a style='color: white; text-decoration: none;' href='https://www.service-public.fr/particuliers/vosdroits/demarches-et-outils/ISE'>Vérifiez votre statut électoral !</a>"
                        "</div>", unsafe_allow_html=True)

    # Countdown timer until 1st of May 2024
    target_date = datetime(2024, 5, 1)
    remaining_time = target_date - datetime.now()

    countdown_placeholder = st.sidebar.empty()

    while remaining_time.total_seconds() > 0:
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_placeholder.markdown(f"<div style='background-color: #FFD700; padding: 8px; border-radius: 5px;'>"
                                      "<div style='color: black; font-size: small;'>"
                                      f"<h3>Temps restant jusqu'au 1er mai 2024 : {days} jours {hours} heures {minutes} minutes {seconds} secondes</h3>"
                                      "</div>"
                                      "</div>", unsafe_allow_html=True)
        remaining_time = target_date - datetime.now()

    countdown_placeholder.markdown("<div style='background-color: #FFD700; padding: 8px; border-radius: 5px;'>"
                                  "<div style='color: black; font-size: small;'>"
                                  "<h3>Le temps est écoulé !</h3>"
                                  "</div>"
                                  "</div>", unsafe_allow_html=True)

    # Sur ce site
    st.subheader("Sur ce site")
    st.write("Bienvenue sur le site de Nostradamus, votre source d'informations essentielles sur les élections européennes. Sur notre plateforme, vous trouverez :")
    st.write("1. **Carte des Résultats** : Explorez une carte interactive des résultats des élections européennes par département afin de visualiser les tendances politiques à travers la France depuis 2004.")
    st.write("2. **Résultats par Commune** : Consultez les résultats des élections européennes de 2014 et 2019 dans votre commune, vous donnant un aperçu détaillé de la participation et des votes pour chaque parti politique.")
    st.write("Notre objectif est de rendre les élections européennes accessibles à tous, afin que chacun puisse prendre des décisions éclairées et participer pleinement à la démocratie européenne.")

    # Répartition
    st.subheader("Répartition par orientation politique")
    st.write("Durant les 20 dernières annnées d'élections européennes, les noms des partis et nuances politiques ont changé considérablement. Pour pouvoir être cohérent dans nos analyses et dans nos prédictions, nous avons décidé de les classer par orientation politique. Nous avons utilisé le site internet de chacun de ces partis et les informations de l'Assemblée Nationale pour effectuer ce tri.")

    # Nos prédictions
    st.subheader("Nos prédictions")
    st.write("Nous sommes des étudiants en Data Analyse à Le Wagon, nous avons entrepris une démarche de collecte de données auprès de Data gouv pour mener nos recherches. Notre objectif est de rendre les élections européennes accessibles à tous, afin que chacun puisse comprendre les enjeux et participer activement à la vie démocratique.")

    # Répartition par année et orientation politique
    st.subheader("Répartition par année et orientation politique")
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
            'Extrême droite': "Prenez le pouvoir, Debout ! La France, Ensemble pour le Frexit",
            'Divers': "Parti animaliste"
        },
        2024: {
            'Extrême gauche': "La France Insoumise, Lutte ouvrière, NPA, PCF",
            'Gauche': "Parti socialiste et Place Publique",
            'Centre gauche': "Europe Ecologie les Verts,Parti radical de Gauche",
            'Centre': "Renaissance, Ecologie au centre",
            'Centre droite': "Alliance rurale",
            'Droite': "Les republicains, Notre Europe",
            'Extrême droite': "Debout ! La France, Reconquête, Rassemblement national, Union populaire republicaine",
            'Divers': "Parti animaliste"
        }
    }

    for year, parties in data.items():
        st.write(f"Année {year} :")
        for party, votes in parties.items():
            st.write(f"- {party} : {votes}")

if __name__ == '__main__':
    main()

