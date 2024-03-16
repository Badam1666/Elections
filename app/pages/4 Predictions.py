import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)

# Nos prédictions
st.subheader("Nos prédictions")
st.write("Pour prédire les résultats des élections de 2024, nous avons utilisé des algorithmes de machine learning, une technologie d'intelligence artificielle qui nous a permis d'analyser les tendances passées et de faire des projections pour 2024. L'algorithme présente quelques limites dans le sens où il ne prend pas en compte le climat politique et social actuel. Vous trouverez ci-dessous nos prévisions que nous avons comparées au sondage Ipsos réalisé au début du mois de mars 2024.")

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
