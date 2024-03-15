import streamlit as st
import time
from datetime import datetime, timedelta

def main():
    st.title("Bienvenue sur le site de Nostradamus")
    st.subheader("Les élections européennes à votre portée")

    # Explication des élections européennes
    st.write("Explication des élections")
    st.write("Les prochaines élections européennes auront lieu du 6 au 9 juin 2024. Vous ne savez pas trop comment ces élections fonctionnent et quels sont leurs enjeux ? Pas d'inquiétude, la team Nostradamus vous aide à y voir plus clair !")
    st.write("Tous les cinq ans, les citoyens des États membres de l'Union européenne votent pour élire leurs représentants au Parlement européen.")
    st.write("Chaque État membre a un nombre de sièges proportionnel à sa population.")
    st.write("Les résultats des élections européennes impactent directement le quotidien des citoyens de l'Union européenne. C'est grâce au Parlement européen que des décisions cruciales pour notre environnement ont été prises, telles que l'interdiction des plastiques à usage unique. De même, le règlement général sur la protection des données (RGPD), adopté par le Parlement européen, renforce nos droits fondamentaux à la vie privée et à la sécurité des données dans un monde de plus en plus numérisé.")
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

 
    # Description du site
    st.header("À propos de Nostradamus")
    st.write("Présentation de notre site, objectif, ce qu'on propose etc")
    st.write("A partir de l'analyse des résultats des élections européennes en France depuis 2004, nous mettons en lumière deux critères qui ont un impact significatif sur les décisions de vote. En utilisant des algorithmes, nous proposons une prédiction des résultats des prochaines élections de juin 2024.")
    
    # Ajout de nouvelles informations
    st.header("Plus sur le site Nostradamus")
    st.write("Sur cette page, vous pouvez trouver les détails de comment nous avons classé les partis politiques en orientations politiques. Sur cette page, vous pouvez trouver une carte des résultats des élections européennes par département de 2004 à 2019. Sur cette page, vous pouvez consulter les résultats de 2014 et 2019 dans votre commune.")
    
    # Nos prévisions
    st.header("Nos Prévisions")
    st.write("Parties du site : Différentes orientations, Carte département")
    st.write("Nous avons regroupé les partis au sein d'orientations politiques. Sur cette carte, vous pouvez consulter les orientations politiques arrivées en tête dans chaque département sur les quatre dernières élections européennes.")
    st.write("Prédictions")
    st.write("A l'image de Nostradamus, célèbre pour ses prédictions sur l'avenir, nous vous proposons des prédictions des résultats des prochaines élections européennes.")

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
            'Centre': "-",
            'Centre droite': "LUCD",
            'Droite': "LUMP, LDVD",
            'Extrême droite': "LFN",
            'Divers': "LCOP, LREG"
        },
        2014: {
            'Extrême gauche': "LFG",
            'Gauche': "LUG",
            'Centre gauche': "LUG",
            'Centre': "-",
            'Centre droite': "LUD",
            'Droite': "LUD",
            'Extrême droite': "LFN",
            'Divers': "LDVD, LDIV"
        },
        2019: {
            'Extrême gauche': "LFG",
            'Gauche': "LUG",
            'Centre gauche': "LUG",
            'Centre': "-",
            'Centre droite': "LUD",
            'Droite': "LUD",
            'Extrême droite': "LRN",
            'Divers': "LDVD, LDIV"
        }
    }

    df = pd.DataFrame(data)
    st.table(df)

if __name__ == '__main__':
    main()
