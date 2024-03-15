import pandas as pd

# Load data
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/Badam1666/Elections/main/raw_data/Elections_Communes_Final.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Function to calculate percentage difference
def calculate_percentage_diff(year1, year2):
    return ((year2 - year1) / year1) * 100

# Streamlit app
st.title('Election Data Explorer')

# Search bar for commune selection
search_query = st.text_input('Search for a commune (code or name):').lower()

# Filter data based on search query
filtered_data = data[data['libelle_commune'].str.lower().str.contains(search_query)]

if not filtered_data.empty:
    # Display filtered data
    st.subheader('Election Data for Selected Commune(s)')
    st.write(filtered_data)

    # Calculate percentage difference for selected commune(s)
    years = filtered_data['annee'].unique()
    if len(years) == 2:
        year1_data = filtered_data[filtered_data['annee'] == years[0]].iloc[:, 2:]
        year2_data = filtered_data[filtered_data['annee'] == years[1]].iloc[:, 2:]
        percentage_diff = calculate_percentage_diff(year1_data, year2_data)

        st.subheader('Percentage Difference Between Years')
        st.write(percentage_diff)
    else:
        st.write('Please select a commune with data for both 2014 and 2019.')

else:
    st.write('No data available for the selected commune.')
