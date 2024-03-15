import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
url = "https://github.com/AliciaD31/elections-nostradamus/blob/main/predictions2024_Python.csv?raw=true"
df = pd.read_csv(url)

# Renomme les orientations politiques
df['Orientation politique'] = df['Orientation politique'].replace({
    'extreme_gauche': 'Extrême gauche',
    'gauche': 'Gauche',
    'centre_gauche': 'Centre gauche',
    'centre': 'Centre',
    'centre_droite': 'Centre droite',
    'droite': 'Droite',
    'extreme_droite': 'Extrême droite',
    'divers': 'Divers'
})

# Define colors for each category
colors = {
    'Divers': '#EEEEEE',
    'Extrême droite': '#242F7F',
    'Droite': '#0066CC',
    'Centre droite': '#82A2C6',
    'Centre': '#ffcc00ff',
    'Centre gauche': '#F3D79A',
    'Gauche': '#FF8080',
    'Extrême gauche': '#BB0000'
}

# Sort dataframe by the percentages
df_sorted_sondages = df.sort_values(by='Sondages_2024', ascending=False)
df_sorted = df.sort_values(by='predictions_2024', ascending=False)

# Create a Streamlit app
st.title('Election Predictions')

# Display the predictions and sondages plots side by side
col1, col2 = st.columns(2)

# Plot for Sondages_2024
with col1:
    plt.figure(figsize=(8, 8))
    plt.barh(df_sorted_sondages['Orientation politique'], df_sorted_sondages['Sondages_2024'], color=[colors.get(x, '#FFFFFF') for x in df_sorted_sondages['Orientation politique']])
    plt.title('Sondages Ipsos - 1-6 mars 2024 - 5169 répondants')
    plt.xlabel('Pourcentage de votes')
    plt.ylabel('Orientation politique')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    for index, value in enumerate(df_sorted_sondages['Sondages_2024']):
        plt.text(value, index, f'{value}%', va='center')
    st.pyplot()

# Plot for predictions_2024
with col2:
    plt.figure(figsize=(8, 8))
    plt.barh(df_sorted['Orientation politique'], df_sorted['predictions_2024'], color=[colors.get(x, '#FFFFFF') for x in df_sorted['Orientation politique']])
    plt.title('Prédictions Nostradamus')
    plt.xlabel('Pourcentage de votes')
    plt.ylabel('Orientation politique')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    for index, value in enumerate(df_sorted['predictions_2024']):
        plt.text(value, index, f'{value}%', va='center')
    st.pyplot()





