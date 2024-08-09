import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

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

# Prepare data for echarts
x_data = count_data['PlasticityIndex'].astype(str).tolist()  # Use strings for x-axis labels
y_data = count_data['Count'].tolist()

# Echarts options
chart_options = {
    "title": {
        "text": "Plasticity Index vs. Count of Samples",
        "subtext": "For OADBY TILL MEMBER"
    },
    "tooltip": {
        "trigger": "axis"
    },
    "xAxis": {
        "type": "category",
        "data": x_data
    },
    "yAxis": {
        "type": "value"
    },
    "series": [
        {
            "name": "Count of Samples",
            "type": "bar",
            "data": y_data
        }
    ]
}

# Render the chart with Streamlit
st.subheader("Plasticity Index vs. Count of Samples for OADBY TILL MEMBER")

st_echarts(options=chart_options)
