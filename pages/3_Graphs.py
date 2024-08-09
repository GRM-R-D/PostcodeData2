import streamlit as st
import pandas as pd
import streamlit_highcharts as hg

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Calculate the mean Plasticity Index for each Date
mean_data = filtered_data.groupby('Date', as_index=False)['PlasticityIndex'].mean()

# Prepare data for Highcharts
chart_data = [[int(d.timestamp() * 1000), pi] for d, pi in mean_data[['Date', 'PlasticityIndex']].values]

# Create Highcharts line chart configuration with curving
chart_options = {
    'chart': {
        'type': 'spline',  # Changed from 'line' to 'spline' for curving
        'zoomType': 'x',
    },
    'title': {
        'text': 'Mean Plasticity Index Over Time for OADBY TILL MEMBER',
        'align': 'center'
    },
    'xAxis': {
        'type': 'datetime',
        'title': {
            'text': 'Date'
        }
    },
    'yAxis': {
        'title': {
            'text': 'Mean Plasticity Index'
        }
    },
    'series': [{
        'name': 'Plasticity Index',
        'data': chart_data,
        'lineWidth': 2,
        'color': '#FF5733',
        'marker': {
            'enabled': False
        },
        'fillOpacity': 0.3
    }],
    'plotOptions': {
        'spline': {  # Updated to 'spline' plot options
            'marker': {
                'enabled': False
            },
        }
    }
}

# Display the Highcharts chart in Streamlit
hg.streamlit_highcharts(chart_options, height=400)
