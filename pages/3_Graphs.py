import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Count occurrences of each Plasticity Index value
count_data = filtered_data['PlasticityIndex'].value_counts().reset_index()
count_data.columns = ['PlasticityIndex', 'Count']

# Display the filtered data (optional)
st.write("Count Data from CSV:")
st.write(count_data)

# Prepare data for streamlit-lightweight-charts
chart_data = count_data[['PlasticityIndex', 'Count']].rename(columns={'PlasticityIndex': 'time', 'Count': 'value'})
chart_data['time'] = chart_data['time'].astype(str)  # Convert Plasticity Index to string

# Chart options
chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

# Series data
seriesLineChart = [{
    "type": 'Line',
    "data": chart_data.to_dict(orient='records'),
    "options": {}
}]

# Render the chart with Streamlit
st.subheader("Count of Plasticity Index Values for OADBY TILL MEMBER")

renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesLineChart
    }
], 'line')
