import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import geemap.foliumap as geemap

# Replace the URL with the correct raw content URL for your pickle file on GitHub
github_pickle_url = 'https://github.com/Badam1666/Elections/raw/main/elections_geo_dpt.pkl'

# Load DataFrame from the pickle file using Pandas
df = pd.read_pickle(github_pickle_url)

# Convert DataFrame to GeoDataFrame using Geopandas
gdf = gpd.GeoDataFrame(df, geometry='geometry')

###########################################################################################################################
# Filter the data by the selected year
selected_year = st.sidebar.selectbox("Select Year", ["2004", "2009", "2014", "2019"])
gdf = gdf[gdf['annee'] == int(selected_year)]

# Set page title
st.title("Map of French Departments with Votes for Each Party")

# Create a Map centered around France
m = geemap.Map(center=[46.603354, 1.888334], zoom=6)

# Define parties
parties = ['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers']

# Sort parties within each department based on the votes, ensuring the most voted party comes first
gdf['winner'] = gdf[parties].idxmax(axis=1)

# Create tooltip fields for winner and results for each party
tooltip_fields = ['nom_departement', 'winner']
tooltip_fields.extend(parties)

# Add GeoDataFrame as choropleth layer to the map
choropleth = folium.GeoJson(
    gdf,
    name='Choropleth',
    style_function=lambda feature: {
        'fillColor': '#EEEEEE' if feature['properties']['winner'] == 'divers' else
                     '#242F7F' if feature['properties']['winner'] == 'extreme_droite' else
                     '#0066CC' if feature['properties']['winner'] == 'droite' else
                     '#82A2C6' if feature['properties']['winner'] == 'centre_droite' else
                     '#FFD700' if feature['properties']['winner'] == 'centre' else
                     '#F3D79A' if feature['properties']['winner'] == 'centre_gauche' else
                     '#FF8080' if feature['properties']['winner'] == 'gauche' else
                     '#BB0000' if feature['properties']['winner'] == 'extreme_gauche' else 'white',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7
    },
    highlight_function=lambda x: {'weight': 3, 'fillOpacity': 1},
    smooth_factor=0,
    tooltip=folium.features.GeoJsonTooltip(fields=tooltip_fields,
                                           aliases=tooltip_fields,
                                           localize=True)
).add_to(m)

# Create legend
legend_html = '''
     <div style="position: fixed; 
                 bottom: 50px; left: 50px; width: 150px; height: 130px; 
                 border:2px solid grey; z-index:9999; font-size:14px;
                 background-color: rgba(255, 255, 255, 0.8);
                ">
     <p style="margin:10px">&nbsp; Legend</p>
     <p style="margin:10px; color:#242F7F">&nbsp; Extrême droite</p>
     <p style="margin:10px; color:#0066CC">&nbsp; Droite</p>
     <p style="margin:10px; color:#82A2C6">&nbsp; Centre droite</p>
     <p style="margin:10px; color:#FFD700">&nbsp; Centre</p>
     <p style="margin:10px; color:#F3D79A">&nbsp; Centre gauche</p>
     <p style="margin:10px; color:#FF8080">&nbsp; Gauche</p>
     <p style="margin:10px; color:#BB0000">&nbsp; Extrême gauche</p>
     <p style="margin:10px; color:#EEEEEE">&nbsp; Divers</p>
      </div>
     '''

m.get_root().html.add_child(folium.Element(legend_html))

# Add layer control
folium.LayerControl().add_to(m)

# Display the map
folium_static(m)
