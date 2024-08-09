import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Count the occurrences of 'OADBY TILL MEMBER' for each Plasticity Index value
count_data = filtered_data.groupby('PlasticityIndex').size().reset_index(name='Count')

# Display the filtered data (optional)
st.write("Count Data:")
st.write(count_data)

# Prepare data for Lightweight Charts
chart_data = count_data.rename(columns={'PlasticityIndex': 'x', 'Count': 'y'})
chart_data = chart_data.sort_values(by='x')

# Convert data to a format suitable for lightweight-charts
data_series = {
    'series': [
        {
            'data': chart_data.to_dict('records'),
            'name': 'Plasticity Index vs Count',
            'type': 'line'
        }
    ]
}

# Create Lightweight Charts configuration
chart_options = {
    'title': 'Plasticity Index vs Count of OADBY TILL MEMBER',
    'xAxis': {'title': 'Plasticity Index'},
    'yAxis': {'title': 'Count'},
    'data': data_series
}

# Render the Lightweight Charts in Streamlit
renderLightweightCharts(chart_options, height='400px')
