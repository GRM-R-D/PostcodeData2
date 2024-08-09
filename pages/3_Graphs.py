import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column (if you have date-related features)
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Count the number of samples for each Plasticity Index value
count_data = filtered_data['PlasticityIndex'].value_counts().reset_index()
count_data.columns = ['PlasticityIndex', 'Count']



# Display the DataFrame
st.write("Plasticity Index Count Data:")
st.write(count_data)

# Prepare data for echarts
x_data = count_data['Count'].tolist()  # Move 'Count' to x-axis
y_data = count_data['PlasticityIndex'].astype(str).tolist()  # Move 'PlasticityIndex' to y-axis

# Echarts options for a line graph with swapped axes
chart_options = {
    "title": {
        "text": "Count of Samples vs. Plasticity Index",
        "subtext": "For OADBY TILL MEMBER"
    },
    "tooltip": {
        "trigger": "axis"
    },
    "xAxis": {
        "type": "value"  # Changed from 'category' to 'value'
    },
    "yAxis": {
        "type": "category",  # Changed from 'value' to 'category'
        "data": y_data  # Use 'PlasticityIndex' as y-axis categories
    },
    "series": [
        {
            "name": "Count of Samples",
            "type": "line",
            "data": list(zip(x_data, y_data))  # Zip 'Count' and 'PlasticityIndex' for correct plotting
        }
    ]
}

# Render the chart with Streamlit
st.subheader("Count of Samples vs. Plasticity Index for OADBY TILL MEMBER")

st_echarts(options=chart_options)
