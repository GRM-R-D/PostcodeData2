import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Calculate the mean Plasticity Index for each Date
mean_data = filtered_data.groupby('Date', as_index=False)['PlasticityIndex'].mean()

# Display the filtered data (optional)
st.write("Filtered Data from CSV:")
st.write(mean_data)

# Create the Vega-Lite chart specification with smooth interpolation
chart_spec = {
    'mark': {
        'type': 'line',
        'interpolate': 'monotone'
    },
    'encoding': {
        'x': {'field': 'Date', 'type': 'temporal', 'title': 'Date'},
        'y': {'field': 'PlasticityIndex', 'type': 'quantitative', 'title': 'Mean Plasticity Index'}
    },
    'title': 'Mean Plasticity Index Over Time for OADBY TILL MEMBER',
    'width': 700,
    'height': 400
}

# Display the chart in Streamlit using st.vega_lite_chart
st.vega_lite_chart(mean_data, spec=chart_spec, use_container_width=True)
