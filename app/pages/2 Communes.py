import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/Badam1666/Elections/main/raw_data/Elections_Communes_Final.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Streamlit app
st.title('Résultat d\'élections dans votre commune')

# Multiselect widget for commune selection
options = data['libelle_commune'].str.lower().unique()
selected_communes = st.sidebar.multiselect('Select Commune(s):', options)

# Filter data based on selected communes
filtered_data = data[data['libelle_commune'].str.lower().isin(selected_communes)]

if not filtered_data.empty:
    # Display filtered data
    st.subheader('Cherchez votre commune dans la barre à gauche pour afficher les résultats de 2014 et 2019 ')

    # Group by commune and sum votes for each party
    grouped_data = filtered_data.groupby(['libelle_commune', 'annee']).sum().reset_index()
    
    # Identify the party that got the most votes for each commune
    max_votes_party = grouped_data[['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite']].idxmax(axis=1)
    grouped_data['Tête'] = max_votes_party

    
    # Rearrange and rename columns
    grouped_data = grouped_data[[
        'libelle_commune', 'annee', 'votants', 'Tête',
        'blancs_et_nuls', 'extreme_gauche', 'gauche', 'centre_gauche',
        'centre', 'centre_droite', 'droite', 'extreme_droite'
    ]]
    grouped_data.columns = ['Commune', 'Année', 'Votants', 'Tête',
                            'Blancs et nuls', 'Extreme gauche', 'Gauche', 'Centre gauche',
                            'Centre', 'Centre droite', 'Droite', 'Extreme droite']
    
    # Replace the year values with "2014" and "2019"
    grouped_data['Année'] = grouped_data['Année'].map({2014: '2014', 2019: '2019'})
    
    # Replace the values in the "Tête" column to match column names
    grouped_data['Tête'] = grouped_data['Tête'].replace({
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
    st.write('No data available for the selected commune(s).')
