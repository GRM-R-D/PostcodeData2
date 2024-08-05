import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Display the data (optional)
st.write("Data from CSV:")
st.write(data)

# Create the Vega-Lite chart specification with smooth interpolation
chart_spec = {
    'mark': {
        'type': 'line',
        'interpolate': 'monotone'
    },
    'encoding': {
        'x': {'field': 'Date', 'type': 'temporal'},
        'y': {'field': 'PlasticityIndex', 'type': 'quantitative'}
    },
    'title': 'Plasticity Index Over Time',
    'width': 700,
    'height': 400
}

# Display the chart in Streamlit using st.vega_lite_chart
st.vega_lite_chart(data, spec=chart_spec, use_container_width=True)
