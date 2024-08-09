import streamlit as st
import pandas as pd
from streamlit_apexcharts import st_apexcharts

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Calculate the mean Plasticity Index for each Date
mean_data = filtered_data.groupby('Date', as_index=False)['PlasticityIndex'].mean()

# Prepare data for ApexCharts
chart_data = [{'x': d, 'y': pi} for d, pi in mean_data[['Date', 'PlasticityIndex']].values]

# Create ApexCharts line chart configuration with curving
chart_options = {
    'chart': {
        'type': 'line',
        'zoom': {
            'enabled': True
        }
    },
    'title': {
        'text': 'Mean Plasticity Index Over Time for OADBY TILL MEMBER',
        'align': 'center'
    },
    'xaxis': {
        'type': 'datetime',
        'title': {
            'text': 'Date'
        }
    },
    'yaxis': {
        'title': {
            'text': 'Mean Plasticity Index'
        }
    },
    'series': [{
        'name': 'Plasticity Index',
        'data': chart_data,
        'color': '#FF5733',
        'lineWidth': 2,
        'fillOpacity': 0.3,
        'smooth': True  # Smoothing the line
    }]
}

# Display the ApexCharts chart in Streamlit
st_apexcharts(options=chart_options, height=400)
