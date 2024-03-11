# Import Streamlit library
import streamlit as st
import pandas as pd
import numpy as np

# Title for the Streamlit app
st.title("Interactive Chart Example")

# Sample data for the chart
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [30, 40, 20, 10]
})

# Display a bar chart
st.bar_chart(data.set_index('Category'))

# Additional text or content
st.write("This is a simple example of an interactive chart in Streamlit.")

