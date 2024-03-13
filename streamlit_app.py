import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px

# Chargement des données
url = "https://raw.githubusercontent.com/Badam1666/Elections/main/Elections_Departements_Final.csv"
df = pd.read_csv(url)

# Chargement de la carte de la France
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filtrer la carte de la France pour ne conserver que les départements français
gdf = gdf[gdf['name'].isin(df['nom_departement'].unique())]

# Fusionner les données des élections avec la carte de la France
merged_data = pd.merge(gdf, df, left_on='name', right_on='nom_departement', how='right')

# Fonction pour obtenir le parti avec le plus grand nombre de voix
def winning_party(row):
    parties = ['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers']
    max_party = max(parties, key=lambda party: row[party])
    return max_party

# Appliquer la fonction pour créer une nouvelle colonne 'winning_party'
merged_data['winning_party'] = merged_data.apply(winning_party, axis=1)

# Filtrer les années uniques
years = df['annee'].unique()
selected_year = st.selectbox("Sélectionner une année", years)

# Filtrer les données par année
filtered_data = merged_data[merged_data['annee'] == selected_year]

# Créer une carte interactive avec Plotly Express
fig = px.choropleth_mapbox(filtered_data, 
                           geojson=filtered_data.geometry, 
                           locations=filtered_data.index, 
                           color='winning_party',
                           hover_data=['nom_departement', 'exprimes', 'abstentions'],
                           mapbox_style="carto-positron",
                           center={"lat": 46.603354, "lon": 1.888334},
                           zoom=4,
                           opacity=0.8,
                           title=f"Résultats des élections européennes {selected_year}")

# Afficher la carte
st.plotly_chart(fig)

# Créer un graphique interactif avec Plotly Express pour l'évolution par parti
fig_evolution = px.line(df, x='annee', y=['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers'], 
                        title="Évolution des votes par parti",
                        labels={'value': 'Pourcentage de votes', 'annee': 'Année', 'variable': 'Parti'})

# Afficher le graphique d'évolution
st.plotly_chart(fig_evolution)

# Afficher les taux d'abstention par département
st.write("Taux d'abstention par département :")
st.dataframe(filtered_data[['nom_departement', 'abstentions']])

# Informations supplémentaires sur le tooltip
st.write("Pourcentage de voix par parti par département (avec un carré de couleur pour chaque parti) :")
st.dataframe(filtered_data[['nom_departement', 'exprimes', 'extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers']])

# Informations sur la population et le revenu médian
st.write("Informations sur la population et le revenu médian :")
st.dataframe(filtered_data[['nom_departement', 'total_pop', 'revenu_median']])
