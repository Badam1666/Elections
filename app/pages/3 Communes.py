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

    # Display heatmap for each year
    for year in filtered_data['annee'].unique():
        year_data = filtered_data[filtered_data['annee'] == year].copy()
        year_data.set_index('libelle_commune', inplace=True)
        year_data.drop(columns=['annee'], inplace=True)

        # Plot heatmap
        fig, ax = plt.subplots(figsize=(10, 6))
        st.write(f'**Year: {year}**')
        sns.heatmap(year_data, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5, ax=ax)
        plt.xlabel('Election Data')
        plt.ylabel('Commune')
        st.pyplot(fig)

else:
    st.write('No data available for the selected commune(s).')
