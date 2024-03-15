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

    # Pivot the data to have years as columns and cities as rows
    pivoted_data = filtered_data.pivot_table(index='libelle_commune', columns='annee', aggfunc='sum').fillna(0)
    
    # Rearrange and rename columns
    pivoted_data = pivoted_data[[
        ('votants', 2014), ('votants', 2019),
        ('taux_participation', 2014), ('taux_participation', 2019),
        ('blancs_et_nuls', 2014), ('blancs_et_nuls', 2019),
        ('extreme_gauche', 2014), ('extreme_gauche', 2019),
        ('gauche', 2014), ('gauche', 2019),
        ('centre_gauche', 2014), ('centre_gauche', 2019),
        ('centre', 2014), ('centre', 2019),
        ('centre_droite', 2014), ('centre_droite', 2019),
        ('droite', 2014), ('droite', 2019),
        ('extreme_droite', 2014), ('extreme_droite', 2019)
    ]]
    pivoted_data.columns = ['Votants 2014', 'Votants 2019',
                            'Taux de participation (%) 2014', 'Taux de participation (%) 2019',
                            'Blancs et nuls 2014', 'Blancs et nuls 2019',
                            'Extreme gauche 2014', 'Extreme gauche 2019',
                            'Gauche 2014', 'Gauche 2019',
                            'Centre gauche 2014', 'Centre gauche 2019',
                            'Centre 2014', 'Centre 2019',
                            'Centre droite 2014', 'Centre droite 2019',
                            'Droite 2014', 'Droite 2019',
                            'Extreme droite 2014', 'Extreme droite 2019']
    
    # Display the DataFrame
    st.write(pivoted_data)

else:
    st.write('No data available for the selected commune(s).')
