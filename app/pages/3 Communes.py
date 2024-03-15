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
st.title('Election Data Explorer')

# Multiselect widget for commune selection
options = data['libelle_commune'].str.lower().unique()
selected_communes = st.sidebar.multiselect('Select Commune(s):', options)

# Filter data based on selected communes
filtered_data = data[data['libelle_commune'].str.lower().isin(selected_communes)]

if not filtered_data.empty:
    # Display filtered data
    st.subheader('Election Data for Selected Commune(s)')

    for commune in selected_communes:
        st.subheader(f'{commune}')

        # Filter data for the current commune
        commune_data = filtered_data[filtered_data['libelle_commune'].str.lower() == commune.lower()]
        
        # Create tables for each metric and concatenate them into a single table
        tables = []
        for metric in ['inscrits', 'taux_participation', 'blancs_et_nuls', 'extreme_gauche', 'gauche',
                       'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers']:
            table = commune_data.pivot(index=None, columns='annee', values=metric)
            table.index = [metric]  # Set index as metric name
            tables.append(table)
        
        table_data = pd.concat(tables)
        st.write(table_data)

else:
    st.write('No data available for the selected commune(s).')
