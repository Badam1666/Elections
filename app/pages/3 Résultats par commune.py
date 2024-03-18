import streamlit as st
import pandas as pd
st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)
# Load data
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/Badam1666/Elections/main/raw_data/Elections_Communes_Final.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Streamlit app
st.title('Résultats des élections européennes par commune')

# Multiselect widget for commune selection
options = data['libelle_commune'].str.lower().unique()
selected_communes = st.sidebar.multiselect('Choisissez une commune :', options)

# Filter data based on selected communes
filtered_data = data[data['libelle_commune'].str.lower().isin(selected_communes)]

if not filtered_data.empty:
    # Display filtered data

    # Group by commune and sum votes for each party
    grouped_data = filtered_data.groupby(['libelle_commune', 'annee']).sum().reset_index()
    
    # Identify the party that got the most votes for each commune
    max_votes_party = grouped_data[['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite']].idxmax(axis=1)
    grouped_data['En tête'] = max_votes_party

    
    # Rearrange and rename columns
    grouped_data = grouped_data[[
        'libelle_commune', 'annee', 'votants', 'En tête',
        'blancs_et_nuls', 'extreme_gauche', 'gauche', 'centre_gauche',
        'centre', 'centre_droite', 'droite', 'extreme_droite'
    ]]
    grouped_data.columns = ['Commune', 'Année', 'Votants', 'En tête',
                            'Blancs et nuls', 'Extreme gauche', 'Gauche', 'Centre gauche',
                            'Centre', 'Centre droite', 'Droite', 'Extreme droite']
    
    # Replace the year values with "2014" and "2019"
    grouped_data['Année'] = grouped_data['Année'].map({2014: '2014', 2019: '2019'})
    
    # Replace the values in the "En tête" column to match column names
    grouped_data['En tête'] = grouped_data['En tête'].replace({
        'extreme_gauche': 'Extreme gauche',
        'gauche': 'Gauche',
        'centre_gauche': 'Centre gauche',
        'centre': 'Centre',
        'centre_droite': 'Centre droite',
        'droite': 'Droite',
        'extreme_droite': 'Extreme droite'
    })
    
    # Set commune as index
    grouped_data.set_index('Commune', inplace=True)
    
    # Display the DataFrame
    st.write(grouped_data)

else:
    st.subheader('Cherchez votre commune dans la barre latérale pour afficher les résultats de 2014 et 2019 ')
