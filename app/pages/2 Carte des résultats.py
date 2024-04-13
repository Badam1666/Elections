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
from datetime import datetime
import time

st.set_page_config(page_title="Elections européennes par département", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)


# Replace the URL with the correct raw content URL for your pickle file on GitHub
github_pickle_url = 'https://github.com/Badam1666/Elections/raw/main/raw_data/elections_geo_dpt.pkl'

# Load DataFrame from the pickle file using Pandas
df = pd.read_pickle(github_pickle_url)

# Convert DataFrame to GeoDataFrame using Geopandas
gdf = gpd.GeoDataFrame(df, geometry='geometry')

###########################################################################################################################
# Filter the data by the selected year
selected_year = st.sidebar.selectbox("Choisissez l'année", ["2004", "2009", "2014", "2019"])
gdf = gdf[gdf['annee'] == int(selected_year)]

# Set page title
st.title("Résultats des élections européennes en France")

# Create a Map centered around France
m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Box bleue avec lien pour vérifier le statut électoral
st.sidebar.markdown("<div style='background-color: #4169E1; padding: 8px; border-radius: 5px; margin-bottom: 10px;'>"
                        "<a style='color: white; text-decoration: none;' href='https://www.service-public.fr/particuliers/vosdroits/demarches-et-outils/ISE'>Vérifiez votre statut électoral !</a>"
                        "</div>", unsafe_allow_html=True)
    
# Box jaune avec countdown
st.sidebar.markdown("<div style='background-color: #FFD700; padding: 8px; border-radius: 5px;'>"
                        "<div style='color: black; font-size: small;'>"
                        "<h3>Temps restant avant la fin des inscriptions en ligne :</h3>"
                        "</div>"
                        "</div>", unsafe_allow_html=True)


# Countdown jusqu'au 1er Mai à minuit
target_datetime = datetime(datetime.now().year, 5, 1, 0, 0)

countdown_placeholder = st.sidebar.empty()

while datetime.now() < target_datetime:
    remaining_time = target_datetime - datetime.now()
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_remaining = f"{days} jours, {hours} heures, {minutes} minutes, {seconds} secondes"
        
    countdown_placeholder.markdown("<div style='background-color: #FFD700; padding: 8px; border-radius: 5px;'>"
                                    "<div style='color: black; font-size: small;'>"
                                    f"<p>{time_remaining}</p>"
                                    "</div>"
                                    "</div>", unsafe_allow_html=True)
        
    time.sleep(1)


# Rename columns
gdf = gdf.rename(columns={'nom_departement': 'Département', 
                          'extreme_droite': 'Extreme droite',
                          'droite': 'Droite',
                          'centre_droite': 'Centre droite',
                          'centre': 'Centre',
                          'centre_gauche': 'Centre gauche',
                          'gauche': 'Gauche',
                          'extreme_gauche': 'Extreme gauche',
                          'divers': 'Divers'})

# Define parties
parties = ['Extreme droite', 'Droite', 'Centre droite', 'Centre', 'Centre gauche', 'Gauche', 'Extreme gauche', 'Divers']

# Sort parties within each department based on the votes, ensuring the most voted party comes first
gdf['En tête'] = gdf[parties].idxmax(axis=1)

# Convert party votes to percentage
for party in parties:
    gdf[f'{party} (%)'] = (gdf[party] / gdf['exprimes']) * 100
    gdf[f'{party} (%)'] = gdf[f'{party} (%)'].round(2)

# Define tooltip fields for each department
tooltip_fields = ['Département', 'En tête']
tooltip_fields.extend([f'{party} (%)' for party in parties])

# Add GeoDataFrame as choropleth layer to the map
choropleth = folium.GeoJson(
    gdf,
    name='Choropleth',
    style_function=lambda feature: {
        'fillColor': '#EEEEEE' if feature['properties']['En tête'] == 'Divers' else
                     '#242F7F' if feature['properties']['En tête'] == 'Extreme droite' else
                     '#0066CC' if feature['properties']['En tête'] == 'Droite' else
                     '#82A2C6' if feature['properties']['En tête'] == 'Centre droite' else
                     '#FFD700' if feature['properties']['En tête'] == 'Centre' else
                     '#F3D79A' if feature['properties']['En tête'] == 'Centre gauche' else
                     '#FF8080' if feature['properties']['En tête'] == 'Gauche' else
                     '#BB0000' if feature['properties']['En tête'] == 'Extreme gauche' else 'white',
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

# Create legend
legend_img = Image.new('RGB', (100, 155), 'white')
draw = ImageDraw.Draw(legend_img)
font = ImageFont.load_default()  # Use default font

# Define legend colors and labels
colors = ['#242F7F', '#0066CC', '#82A2C6', '#FFD700', '#F3D79A', '#FF8080', '#BB0000', '#EEEEEE']
labels = ['Extreme droite', 'Droite', 'Centre droite', 'Centre', 'Centre gauche', 'Gauche', 'Extreme gauche', 'Divers']

# Draw legend
for i, (color, label) in enumerate(zip(colors, labels)):
    y = i * 20
    draw.rectangle([0, y, 10, y + 10], fill=color)
    draw.text((15, y), label, font=font, fill='black')

# Display the map and legend
col1, col2 = st.columns([6,1])
with col1:
    folium_static(m, width=800, height=600)

with col2:
    st.image(legend_img, caption="Legend", use_column_width=True)
