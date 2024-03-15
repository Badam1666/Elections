import pandas as pd
import streamlit as st

# Create the original data dictionary
data = {
    'Année': ['2004-01-01', '2009-01-01', '2014-01-01', '2019-01-01', '2024-01-01'],
    'extreme_gauche': ['Liste pour la gauche antilibérale', 'Front de gauche', 'Front de gauche', 'La France Insoumise', 'La France Insoumise'],
    'gauche': ['Parti socialiste', 'Parti socialiste', 'Parti socialiste', 'Liste PS PRG MDM', 'Parti socialiste'],
    'centre_gauche': ['Les Verts', 'Europe Ecologie', 'Europe Écologie', 'Europe Écologie Les Verts', 'Europe Écologie Les Verts'],
    'centre': ['-', 'MoDem', 'Parti radical de gauche', 'Renaissance', 'Renaissance'],
    'centre_droite': ['UDF', '-', '-', 'Union de la droite et du centre', 'Les Républicains'],
    'droite': ['UMP', 'UMP', 'UMP', '-', 'Union de la droite et du centre'],
    'extreme_droite': ['Front National', 'Front National', 'Front National', 'Rassemblement National', 'Rassemblement National'],
    'divers': ['-', '-', 'Debout la République', 'Debout la France', 'Debout la France']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the data as a list per year
st.title("Résultats des Élections Européennes")
st.write("Voici les résultats des élections européennes par année :")
for index, row in df.iterrows():
    st.write(f"Année : {row['Année']}")
    st.write("- Extrême gauche :", row['extreme_gauche'])
    st.write("- Gauche :", row['gauche'])
    st.write("- Centre gauche :", row['centre_gauche'])
    st.write("- Centre :", row['centre'])
    st.write("- Centre droite :", row['centre_droite'])
    st.write("- Droite :", row['droite'])
    st.write("- Extrême droite :", row['extreme_droite'])
    st.write("- Divers :", row['divers'])
    st.write("\n")
