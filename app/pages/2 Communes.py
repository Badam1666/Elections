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

    # Filter data for the years 2014 and 2019
    filtered_data = filtered_data[filtered_data['annee'].isin([2014, 2019])]
    
    # Group data by commune and year to get party percentages
    grouped_data = filtered_data.groupby(['libelle_commune', 'annee']).sum().reset_index()
    
    # Create a DataFrame to store the results
    df = grouped_data.pivot(index='libelle_commune', columns='annee', values=['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers']).fillna(0)
    df.columns = ['_'.join(map(str, col)).strip() for col in df.columns.values]
    df.reset_index(inplace=True)
    
    # Display the DataFrame
    st.write(df)

else:
    st.write('No data available for the selected commune(s).')
