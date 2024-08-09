import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Count occurrences of each Plasticity Index value
count_data = filtered_data['PlasticityIndex'].value_counts().reset_index()
count_data.columns = ['PlasticityIndex', 'Count']

# Display the filtered data (optional)
st.write("Count Data from CSV:")
st.write(count_data)

# Prepare data for Lightweight Charts
# Convert Plasticity Index to string for proper display
chart_data = count_data.rename(columns={'PlasticityIndex': 'x', 'Count': 'y'})
chart_data['x'] = chart_data['x'].astype(str)  # Convert to string if needed

# Chart options
chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    },
    "xAxis": {
        "title": "Plasticity Index",
        "type": "category"  # Category type if x-axis is categorical
    },
    "yAxis": {
        "title": "Count"
    }
}

# Series data
seriesLineChart = [{
    "type": 'Line',
    "data": chart_data.to_dict(orient='records'),
    "options": {
        "color": 'blue',
        "lineWidth": 2
    }
}]

# Render the chart with Streamlit
st.subheader("Count of Plasticity Index Values for OADBY TILL MEMBER")

renderLightweightCharts({
    "chart": chartOptions,
    "series": seriesLineChart
})
