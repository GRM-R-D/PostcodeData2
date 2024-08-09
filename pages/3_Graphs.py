import streamlit as st
import pandas as pd
import streamlit_gchart as gchart

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Calculate the mean Plasticity Index for each Date
mean_data = filtered_data.groupby('Date', as_index=False)['PlasticityIndex'].mean()

# Prepare data for Google Charts
chart_data = [['Date', 'Mean Plasticity Index']] + [[d.strftime('%Y-%m-%d'), pi] for d, pi in mean_data[['Date', 'PlasticityIndex']].values]

# Define the GChart options
chart_options = {
    'title': 'Mean Plasticity Index Over Time for OADBY TILL MEMBER',
    'curveType': 'function',  # This adds the smoothing effect
    'legend': {'position': 'bottom'},
    'hAxis': {'title': 'Date'},
    'vAxis': {'title': 'Mean Plasticity Index'},
    'height': 400,
}

# Display the chart using streamlit-gchart
gchart.gchart(data=chart_data, options=chart_options)
