# Raw content URL for an Excel file
github_excel_url = 'https://github.com/Badam1666/Elections/raw/main/elections_geo_dpt.xlsx'

# Read Excel file into a DataFrame
df = pd.read_excel(github_excel_url)

print(df.info())
