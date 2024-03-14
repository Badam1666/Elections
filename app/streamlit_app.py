import streamlit as st
import pandas as pd
import geopandas as gpd

github_pickle_url = 'https://github.com/Badam1666/Elections/raw/main/elections_geo_dpt.pkl'

"Hello"

# Load DataFrame from the pickle file using Pandas
df = pd.read_pickle(github_pickle_url)

# Convert DataFrame to GeoDataFrame using Geopandas
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# Display the GeoDataFrame in Streamlit
st.write(gdf)
