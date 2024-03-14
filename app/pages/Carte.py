
import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import geemap.foliumap as geemap
from PIL import Image, ImageDraw, ImageFont
import io

# Replace the URL with the correct raw content URL for your pickle file on GitHub
github_pickle_url = 'https://github.com/Badam1666/Elections/raw/main/raw_data/elections_geo_dpt.pkl'

# Load DataFrame from the pickle file using Pandas
df = pd.read_pickle(github_pickle_url)

# Convert DataFrame to GeoDataFrame using Geopandas
gdf = gpd.GeoDataFrame(df, geometry='geometry')

###########################################################################################################################
# Filter the data by the selected year
selected_year = st.sidebar.selectbox("Select Year", ["2004", "2009", "2014", "2019"])
gdf = gdf[gdf['annee'] == int(selected_year)]

# Set page title
st.title("Résultats des élections européennes en France")

# Create a Map centered around France
m = geemap.Map(center=[46.603354, 1.888334], zoom=6)

# Define parties
parties = ['extreme_gauche', 'gauche', 'centre_gauche', 'centre', 'centre_droite', 'droite', 'extreme_droite', 'divers']

# Sort parties within each department based on the votes, ensuring the most voted party comes first
gdf['Tête'] = gdf[parties].idxmax(axis=1)

# Convert party votes to percentage
for party in parties:
    gdf[f'{party} (%)'] = (gdf[party] / gdf['exprimes']) * 100
    gdf[f'{party} (%)'] = gdf[f'{party} (%)'].round(2)

# Rename columns
gdf = gdf.rename(columns={'nom_departement': 'Département', 
                          'extreme_droite': 'Extrême droite',
                          'droite': 'Droite',
                          'centre_droite': 'Centre droite',
                          'centre': 'Centre',
                          'centre_gauche': 'Centre gauche',
                          'gauche': 'Gauche',
                          'extreme_gauche': 'Extrême gauche',
                          'divers': 'Divers'})

# Define tooltip fields for each department
tooltip_fields = ['Département', 'Tête']
tooltip_fields.extend([f'{party} (%)' for party in parties])

# Add GeoDataFrame as choropleth layer to the map
choropleth = folium.GeoJson(
    gdf,
    name='Choropleth',
    style_function=lambda feature: {
        'fillColor': '#EEEEEE' if feature['properties']['Tête'] == 'divers' else
                     '#242F7F' if feature['properties']['Tête'] == 'extreme_droite' else
                     '#0066CC' if feature['properties']['Tête'] == 'droite' else
                     '#82A2C6' if feature['properties']['Tête'] == 'centre_droite' else
                     '#FFD700' if feature['properties']['Tête'] == 'centre' else
                     '#F3D79A' if feature['properties']['Tête'] == 'centre_gauche' else
                     '#FF8080' if feature['properties']['Tête'] == 'gauche' else
                     '#BB0000' if feature['properties']['Tête'] == 'extreme_gauche' else 'white',
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

# Add layer control
folium.LayerControl().add_to(m)

# Display the map
folium_static(m)

# Create legend
legend_img = Image.new('RGB', (100, 300), 'white')
draw = ImageDraw.Draw(legend_img)
font = ImageFont.truetype("arial.ttf", 12)

# Define legend colors and labels
colors = ['#242F7F', '#0066CC', '#82A2C6', '#FFD700', '#F3D79A', '#FF8080', '#BB0000', '#EEEEEE']
labels = ['Extrême droite', 'Droite', 'Centre droite', 'Centre', 'Centre gauche', 'Gauche', 'Extrême gauche', 'Divers']

# Draw legend
for i, (color, label) in enumerate(zip(colors, labels)):
    y = i * 30
    draw.rectangle([0, y, 20, y + 20], fill=color)
    draw.text((30, y), label, font=font, fill='black')

# Display the legend
st.sidebar.image(legend_img, caption="Legend", use_column_width=True)
