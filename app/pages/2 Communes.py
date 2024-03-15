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
    
    # Plot heatmap
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivoted_data, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5, ax=ax)
    plt.xlabel('Year')
    plt.ylabel('Commune')
    st.pyplot(fig)

else:
    st.write('No data available for the selected commune(s).')
