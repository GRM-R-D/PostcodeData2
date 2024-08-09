import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Count the number of samples for each Plasticity Index value
count_data = filtered_data['PlasticityIndex'].value_counts().reset_index()
count_data.columns = ['PlasticityIndex', 'Count']

# Display the filtered data (optional)
st.write("Plasticity Index Count Data:")
st.write(count_data)

# Prepare data for streamlit-lightweight-charts
# Convert to dict format suitable for Lightweight Charts
chart_data = count_data[['PlasticityIndex', 'Count']].rename(columns={'PlasticityIndex': 'time', 'Count': 'value'})
chart_data = chart_data.to_dict(orient='records')

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
            "formatter": "function(value) { return value; }"  # Show Plasticity Index values directly
        }
    }
}

# Series data
seriesLineChart = [{
    "name": "Count of Samples",
    "data": chart_data,
    "type": 'bar',  # Using 'bar' for count of samples
    "options": {}
}]

# Render the chart with Streamlit
st.subheader("Plasticity Index vs. Count of Samples for OADBY TILL MEMBER")

renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesLineChart
    }
], 'bar')  # Using 'bar' to visualize counts
