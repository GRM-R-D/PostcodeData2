import streamlit as st
import pandas as pd
from streamlit_apexjs import st_apexcharts

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

# Prepare data for ApexCharts
dates = mean_data['Date'].dt.strftime('%Y-%m-%d').tolist()  # Convert to string format for labels
plasticity_indices = mean_data['PlasticityIndex'].tolist()

# Create ApexCharts line chart specification
options = {
    "chart": {
        "type": "line",
        "zoom": {"enabled": True}
    },
    "title": {
        "text": "Mean Plasticity Index Over Time for OADBY TILL MEMBER",
        "align": "center"
    },
    "xaxis": {
        "categories": dates,
        "title": {"text": "Date"}
    },
    "yaxis": {
        "title": {"text": "Mean Plasticity Index"}
    },
    "dataLabels": {"enabled": False},
    "tooltip": {"enabled": True}
}

# Display the ApexCharts chart in Streamlit
st_apexcharts(
    options=options,
    series=[{"name": "Plasticity Index", "data": plasticity_indices}],
    width='600px',
    title='Mean Plasticity Index Over Time'
)
