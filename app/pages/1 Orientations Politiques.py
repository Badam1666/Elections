import pandas as pd
import streamlit as st

# Create the original data dictionary
data = {
    'Année': [2004, 2009, 2014, 2019, 2024],
    'Extrême gauche': ["LPC, LXG", "LEXG, LCOP", "LEXG, LFG", "La France Insoumise, L'Europe des gens", "La France Insoumise, Lutte ouvrière, NPA, PCF"],
    'Gauche': ["LPS, LDG", "LSOC, LDVD", "LDVG, LUG", "Liste citoyenne",  "Parti socialiste et Place Publique"],
    'Centre gauche': ["LEC, LVE", "LVEC", "LVEC", "Europe Ecologie, Envie d'Europe, Urgence Ecologie", "Europe Ecologie les Verts,Parti radical de Gauche "],
    'Centre': ["-","LCMD", "LUC", "Renaissance", "Renaissance, Ecologie au centre"],
    'Centre droite': ["LUDF", "-", "-", "Union Droite Centre, Les européens", "Alliance rurale"],
    'Droite': ["LUMP, LCP, LDD", "LMAJ, LDVD", "LDVD, LUMP", "-", "Les republicains, Notre Europe"],
    'Extrême droite': ["LFN, LXD", "LFN, LEXD", "LFN, LEXD", " Prenez le pouvoir, Debout ! La France, Ensemble pour le Frexit", "Debout ! La France, Reconquête, Rassemblement national, Union populaire republicaine"],
    'Divers': ["LDV, LRG", " LAUT, LREG", "LDIV", "Parti animaliste", "Parti animaliste"]
}
# Create a DataFrame from the data
df = pd.DataFrame(data)
# Reshape the DataFrame
reshaped_df = pd.melt(df, id_vars=['Année'], var_name='Orientation Politique', value_name='Partis')
# Pivot the reshaped DataFrame
pivoted_df = reshaped_df.pivot(index='Année', columns='Orientation Politique', values='Partis')

# Display the pivoted DataFrame using Streamlit
st.write("Voici le DataFrame pivoté :")
st.write(pivoted_df)
