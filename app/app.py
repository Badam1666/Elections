import streamlit as st
import time
from datetime import datetime, timedelta

def main():
    st.title("Bienvenue sur le site de Nostradamus")
    st.subheader("Les élections européennes à votre portée")

    # Explication des élections européennes
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

    # Sur ce site
    st.title("Sur ce site")
    st.write("Bienvenue sur le site de Nostradamus, votre source d'informations essentielles sur les élections européennes. Sur notre plateforme, vous trouverez :")
    st.write("1. **Orientations Politiques** : Découvrez comment nous classons les partis politiques en différentes orientations politiques, vous permettant de mieux comprendre les différentes idéologies et positions sur les questions européennes.")
    st.write("2. **Carte des Résultats** : Explorez une carte interactive des résultats des élections européennes par département, vous permettant de visualiser les tendances politiques à travers la France depuis 2004.")
    st.write("3. **Résultats par Commune** : Consultez les résultats des élections européennes de 2014 et 2019 dans votre commune, vous donnant un aperçu détaillé de la participation et des votes pour chaque parti politique.")
    st.write("Notre objectif est de rendre les élections européennes accessibles à tous, afin que chacun puisse prendre des décisions éclairées et participer pleinement à la démocratie européenne.")

    # Nos prévisions
    st.header("Nos Prévisions")
    st.write("Nous sommes des étudiants à Le Wagon, une école de codage renommée, et nous avons entrepris une démarche de collecte de données auprès de Data gouv pour mener nos recherches. Notre objectif est de rendre les élections européennes accessibles à tous, afin que chacun puisse comprendre les enjeux et participer activement à la vie démocratique.")
    st.write("Pour prédire les élections de 2024, nous avons utilisé des algorithmes de machine learning, une approche moderne qui nous a permis d'analyser les tendances passées et de faire des projections pour l'avenir. Cependant, l'algorithme ne prend pas en compte le climat politique et social et a ses limites dans la prédiction de futures élections. Vous trouverez ci-dessous les prévisions de Nostradamus, notre plateforme de prédiction, comparées aux sondages Ipsos réalisés au début du mois de Mars.")

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

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
url = "https://github.com/AliciaD31/elections-nostradamus/blob/main/predictions2024_Python.csv?raw=true"
df = pd.read_csv(url)

# Renomme les orientations politiques
df['Orientation politique'] = df['Orientation politique'].replace({
    'extreme_gauche': 'Extrême gauche',
    'gauche': 'Gauche',
    'centre_gauche': 'Centre gauche',
    'centre': 'Centre',
    'centre_droite': 'Centre droite',
    'droite': 'Droite',
    'extreme_droite': 'Extrême droite',
    'divers': 'Divers'
})

# Define colors for each category
colors = {
    'Divers': '#EEEEEE',
    'Extrême droite': '#242F7F',
    'Droite': '#0066CC',
    'Centre droite': '#82A2C6',
    'Centre': '#ffcc00ff',
    'Centre gauche': '#F3D79A',
    'Gauche': '#FF8080',
    'Extrême gauche': '#BB0000'
}

# Sort dataframe by the percentages
df_sorted_sondages = df.sort_values(by='Sondages_2024', ascending=True)
df_sorted = df.sort_values(by='predictions_2024', ascending=True)

# Create a Streamlit app
st.title('Election Predictions')

# Display the predictions and sondages plots side by side
col1, col2 = st.columns(2)

# Plot for predictions_2024
with col1:
    fig1, ax1 = plt.subplots(figsize=(8, 8))
    ax1.barh(df_sorted['Orientation politique'], df_sorted['predictions_2024'], color=[colors.get(x, '#FFFFFF') for x in df_sorted['Orientation politique']])
    ax1.set_title('Prédictions Nostradamus')
    ax1.set_xlabel('Pourcentage de votes')
    ax1.set_ylabel('Orientation politique')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    for index, value in enumerate(df_sorted['predictions_2024']):
        ax1.text(value, index, f'{value}%', va='center')
    st.pyplot(fig1)

# Plot for Sondages_2024
with col2:
    fig2, ax2 = plt.subplots(figsize=(8, 8))
    ax2.barh(df_sorted_sondages['Orientation politique'], df_sorted_sondages['Sondages_2024'], color=[colors.get(x, '#FFFFFF') for x in df_sorted_sondages['Orientation politique']])
    ax2.set_title('Sondages Ipsos - 1-6 mars 2024 - 5169 répondants')
    ax2.set_xlabel('Pourcentage de votes')
    ax2.set_ylabel('Orientation politique')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    for index, value in enumerate(df_sorted_sondages['Sondages_2024']):
        ax2.text(value, index, f'{value}%', va='center')
    st.pyplot(fig2)

if __name__ == '__main__':
    main()
