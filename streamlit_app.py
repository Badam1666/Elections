# Import Streamlit library
import streamlit as st

# Title for the Streamlit app
st.title("Interactive Map Example")

# Sample data (latitude, longitude, marker label)
data = [
    (37.7749, -122.4194, "Marker 1"),
    (34.0522, -118.2437, "Marker 2"),
    (40.7128, -74.0060, "Marker 3"),
]

# Display the map with markers
st.map(data)

# Additional text or content
st.write("This is a simple example of an interactive map in Streamlit.")
