import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/Badam1666/Elections/main/raw_data/Elections_Communes_Final.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Streamlit app
st.title('Election Data Explorer')
st.subheader('Recherchez votre commune dans la barre de gauche pour afficher les résultats des années 2014 et 2019')

# Multiselect widget for commune selection
options = data['libelle_commune'].unique()
selected_communes = st.sidebar.multiselect('Sélectionnez votre commune(s):', options)

# Filter data based on selected communes
filtered_data = data[data['libelle_commune'].isin(selected_communes)]

if not filtered_data.empty:
    # Display filtered data
    st.subheader('Données électorales pour les communes sélectionnées')

    # Group by commune and year to get party percentages
    grouped_data = filtered_data.groupby(['libelle_commune', 'annee']).sum().reset_index()

    # Pivot the data to have years as columns and cities as rows
    pivoted_data = grouped_data.pivot(index='libelle_commune', columns='annee', values=['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers']).fillna(0)
    pivoted_data.columns = ['_'.join(map(str, col)).strip() for col in pivoted_data.columns.values]
    
    # Add party percentage columns for each year
    for party in ['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers']:
        pivoted_data[f'{party}_percentage_2014'] = (pivoted_data[f'{party}_2014'] / pivoted_data['total_votes_2014']) * 100
        pivoted_data[f'{party}_percentage_2019'] = (pivoted_data[f'{party}_2019'] / pivoted_data['total_votes_2019']) * 100

    # Determine the winner party for each commune
    pivoted_data['Winner'] = pivoted_data[['extreme_gauche_percentage_2019', 'gauche_percentage_2019', 'centre_gauche_percentage_2019', 'centre_percentage_2019', 'centre_droite_percentage_2019', 'droite_percentage_2019', 'extreme_droite_percentage_2019', 'divers_percentage_2019']].idxmax(axis=1)
    
    # Display results
    st.write('Résultats des élections par commune:')
    st.write(pivoted_data)

else:
    st.write('Aucune donnée disponible pour la ou les communes sélectionnées.')
