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
selected_communes = st.sidebar.multiselect('Search and Select Commune(s):', 
                                            data['libelle_commune'].unique())

# Filter data based on selected communes
filtered_data = data[data['libelle_commune'].isin(selected_communes)]

if not filtered_data.empty:
    # Display filtered data
    st.subheader('Election Data for Selected Commune(s)')

    # Display data for each year
    for year in filtered_data['annee'].unique():
        year_data = filtered_data[filtered_data['annee'] == year].iloc[:, 2:]
        
        # Display data in a table format
        st.write(f'**Year: {year}**')
        st.write(year_data)

    # Calculate percentage difference for selected commune(s)
    years = filtered_data['annee'].unique()
    if len(years) == 2:
        year1_data = filtered_data[filtered_data['annee'] == years[0]].iloc[:, 2:]
        year2_data = filtered_data[filtered_data['annee'] == years[1]].iloc[:, 2:]
        percentage_diff = ((year2_data - year1_data) / year1_data) * 100

        st.subheader('Percentage Difference Between Years')
        st.write(percentage_diff)
    else:
        st.write('Please select a commune with data for both 2014 and 2019.')

else:
    st.write('No data available for the selected commune(s).')
