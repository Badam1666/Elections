import streamlit as st
import pandas as pd

# Replace this URL with the correct raw content URL for your Excel file on GitHub
github_excel_url = 'https://github.com/Badam1666/Elections/raw/main/elections_geo_dpt.xlsx'

# Read Excel file into a DataFrame
df = pd.read_excel(github_excel_url)

# Display the DataFrame in Streamlit
st.dataframe(df)
