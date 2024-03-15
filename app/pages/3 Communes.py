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
        
        # Calculate total votes for each year
        commune_data['total_votes'] = commune_data[['extreme_gauche', 'gauche', 'centre_gauche', 
                                                    'centre', 'centre_droite', 'droite', 
                                                    'extreme_droite', 'divers']].sum(axis=1)
        
        # Calculate percentage of each type of vote
        vote_types = ['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 
                      'centre_droite', 'droite', 'extreme_droite', 'divers']
        for vote_type in vote_types:
            commune_data[f'{vote_type}_percentage'] = (commune_data[vote_type] / commune_data['total_votes']) * 100
        
        # Determine the party with the most votes for each year
        commune_data['Tête'] = commune_data[vote_types].idxmax(axis=1)
        
        # Create a table with metrics as rows and years as columns
        table_data = {}
        for metric in vote_types + [f'{vote_type}_percentage' for vote_type in vote_types] + ['Tête']:
            metric_data = {}
            for year in [2014, 2019]:
                year_data = commune_data[commune_data['annee'] == year]
                if not year_data.empty:
                    metric_data[year] = year_data[metric].values[0] if metric in year_data else 0
                else:
                    metric_data[year] = 0
            table_data[metric] = metric_data
        
        table_df = pd.DataFrame(table_data)
        st.write(table_df)

else:
    st.write('No data available for the selected commune(s).')
