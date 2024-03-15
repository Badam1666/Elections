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
st.title('Répartition des votes par commune')
st.subheader('Recherchez votre commune dans la barre de gauche pour afficher les résultats des années 2014 et 2019')

# Multiselect widget for commune selection
options = data['libelle_commune'].str.lower().unique()
selected_communes = st.sidebar.multiselect('Sélectionnez votre commune(s):', options)

# Filter data based on selected communes
filtered_data = data[data['libelle_commune'].str.lower().isin(selected_communes)]

if not filtered_data.empty:
    # Display filtered data
    st.subheader('Données électorales pour la ou les communes sélectionnées')

    for commune in selected_communes:
        st.subheader(f'{commune}')

        # Filter data for the current commune
        commune_data = filtered_data[filtered_data['libelle_commune'].str.lower() == commune.lower()]
        
        # Create a dictionary to store party percentages for each year
        party_percentages = {}
        for year in [2014, 2019]:
            year_data = commune_data[commune_data['annee'] == year]
            if not year_data.empty:
                total_votes = year_data.iloc[0][2:].sum()  # Assuming the vote columns start from 3rd column
                party_percentages[year] = {party: (year_data.iloc[0][party] / total_votes) * 100 if total_votes != 0 else 0 for party in ['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite']}
            else:
                party_percentages[year] = {}
        
        # Create DataFrame from party percentages
        party_df = pd.DataFrame.from_dict(party_percentages).transpose()
        party_df = party_df.rename(columns={party: f'{party}_percentage' for party in party_df.columns})
        
        # Add year columns to the DataFrame
        party_df['2014'] = party_df.index.map(lambda x: x['extreme_gauche_percentage'] if 'extreme_gauche_percentage' in x else 0)
        party_df['2019'] = party_df.index.map(lambda x: x['extreme_gauche_percentage'] if 'extreme_gauche_percentage' in x else 0)
        
        # Compute total votes, null votes, and winner party
        total_votes = commune_data['votants'].sum()
        null_votes = commune_data['null'].sum()
        winner_party = commune_data.iloc[0]['Tête']
        
        # Create a DataFrame for additional information
        info_df = pd.DataFrame({
            'Métrique': ['Total des votes', 'Votes nuls/blancs', 'Parti gagnant'],
            'Valeur': [total_votes, null_votes, winner_party]
        })
        
        # Display party percentages, votants, null, and additional information
        st.write('Répartition des votes par parti:')
        st.write(party_df)
        st.write('Votes (votants) et nuls/blancs:')
        st.write(commune_data[['libelle_commune', 'votants', 'null']])
        st.write('Informations supplémentaires:')
        st.write(info_df)

else:
    st.write('Aucune donnée disponible pour la ou les communes sélectionnées.')
