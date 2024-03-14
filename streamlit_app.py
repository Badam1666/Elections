import streamlit as st
import pandas as pd

github_pickle_url = 'https://github.com/Badam1666/Elections/raw/main/elections_geo_dpt.pkl'

# Load DataFrame from the pickle file
df = pd.read_pickle(github_pickle_url)

df.info()

# Display the DataFrame in Streamlit
st.dataframe(df)
