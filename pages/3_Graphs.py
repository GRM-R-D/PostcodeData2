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

# Convert data to format suitable for Lightweight Charts
chart_data = count_data.rename(columns={'PlasticityIndex': 'x', 'Count': 'y'})

# Prepare chart options and series data
chart_options = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    },
    "xAxis": {
        "title": "Plasticity Index"
    },
    "yAxis": {
        "title": "Count"
    }
}

series_line_chart = {
    "type": 'Line',
    "data": chart_data.to_dict(orient='records'),
    "options": {
        "color": 'blue',
        "lineWidth": 2
    }
}

# Render the chart
st.subheader("Plasticity Index vs Count of OADBY TILL MEMBER")

renderLightweightCharts({
    "chart": chart_options,
    "series": [series_line_chart]
})
