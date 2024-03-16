import streamlit as st
import pandas as pd

st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)

# Répartition
st.subheader("Répartion par orientation politique")
    
st.write("Durant les 20 dernières annnées d'élections européennes, les noms des partis et nuances politiques ont changé considérablement. Pour pouvoir être cohérent dans nos analyses et dans nos prédictions, nous avons décidé de les classer par orientation politique. Nous avons utilisé le site internet de chacun de ces partis et les informations de l'Assemblée Nationale pour effectuer ce tri.")
data = {
    2004: {
        'Extrême gauche': "LPC, LXG",
        'Gauche': "LPS, LDG",
        'Centre gauche': "LEC, LVE",
        'Centre': "-",
        'Centre droite': "LUDF",
        'Droite': "LUMP, LCP, LDD",
        'Extrême droite': "LFN, LXD",
        'Divers': "LDV, LRG"
    },
    2009: {
        'Extrême gauche': "LEXG, LCOP",
        'Gauche': "LSOC, LDVD",
        'Centre gauche': "LVEC",
        'Centre': "LCMD",
        'Centre droite': "-",
        'Droite': "LMAJ, LDVD",
        'Extrême droite': "LFN, LEXD",
        'Divers': "LAUT, LREG"
    },
    2014: {
        'Extrême gauche': "LEXG, LFG",
        'Gauche': "LDVG, LUG",
        'Centre gauche': "LVEC",
        'Centre': "LUC",
        'Centre droite': "-",
        'Droite': "LDVD, LUMP",
        'Extrême droite': "LFN, LEXD",
        'Divers': "LDIV"
    },
    2019: {
        'Extrême gauche': "La France Insoumise, L'Europe des gens",
        'Gauche': "Liste citoyenne",
        'Centre gauche': "Europe Ecologie, Envie d'Europe, Urgence Ecologie",
        'Centre': "Renaissance",
        'Centre droite': "Union Droite Centre, Les européens",
        'Droite': "-",
        'Extrême droite': "Prenez le pouvoir (RN), Debout ! La France, Ensemble pour le Frexit",
        'Divers': "Parti animaliste"
    },
    2024: {
        'Extrême gauche': "La France Insoumise, Lutte ouvrière, NPA, PCF",
        'Gauche': "Parti socialiste et Place Publique",
        'Centre gauche': "Europe Ecologie les Verts,Parti radical de Gauche",
        'Centre': "Renaissance, Ecologie au centre",
        'Centre droite': "Alliance rurale",
        'Droite': "Les republicains, Notre Europe",
        'Extrême droite': "Debout ! La France, Reconquête, Rassemblement national, Union populaire républicaine",
        'Divers': "Parti animaliste"
    }
}

df = pd.DataFrame(data)
st.table(df)

