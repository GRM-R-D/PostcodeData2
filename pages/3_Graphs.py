import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

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

# Prepare data for streamlit-lightweight-charts
# Convert dates to Unix timestamps
mean_data['Date'] = mean_data['Date'].astype(int) // 10**9  # Convert to Unix timestamp in seconds

# Convert to dict format suitable for Lightweight Charts
chart_data = mean_data[['Date', 'PlasticityIndex']].rename(columns={'Date': 'time', 'PlasticityIndex': 'value'})
chart_data['time'] = chart_data['time'].astype(str)  # Convert datetime to string

# Chart options with custom date formatting
chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    },
    "xAxis": {
        "labels": {
            "formatter": "function(value) { return new Date(value * 1000).toLocaleDateString('en-GB'); }"  # Format timestamp to D-M-YYYY
        }
    }
}

# Series data
seriesLineChart = [{
    "name": "Plasticity Index",
    "data": chart_data,
    "type": 'line',
    "options": {}
}]

# Render the chart with Streamlit
st.subheader("Mean Plasticity Index Over Time for OADBY TILL MEMBER")

renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesLineChart
    }
], 'line')
