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
search_query = st.sidebar.text_input('Search for a commune (code or name):').lower()

# Filter options based on search query
options = data['libelle_commune'].str.lower().unique()
suggested_options = [option for option in options if search_query in option]

# Multiselect widget for commune selection
selected_communes = st.sidebar.multiselect('Select Commune(s):', suggested_options)

# Filter data based on selected communes
filtered_data = data[data['libelle_commune'].str.lower().isin(selected_communes)]

if not filtered_data.empty:
    # Display filtered data
    st.subheader('Election Data for Selected Commune(s)')

    # Display data for each year
    for year in filtered_data['annee'].unique():
        year_data = filtered_data[filtered_data['annee'] == year].iloc[:, 2:]
        
        # Display data as a list
        st.write(f'**Year: {year}**')
        for index, row in year_data.iterrows():
            st.write("- ".join([f"{col}: {row[col]}" for col in year_data.columns]))

else:
    st.write('No data available for the selected commune(s).')
