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

    # Pivot the data to have years as columns and cities as rows
    pivoted_data = filtered_data.pivot_table(index='libelle_commune', columns='annee', aggfunc='sum').fillna(0)
    
    # Convert the pivot table to a DataFrame
    df = pivoted_data.reset_index()
    df.columns.name = None  # Remove the name of the columns index
    
    # Display the DataFrame
    st.write(df)

else:
    st.write('No data available for the selected commune(s).')
