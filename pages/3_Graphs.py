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

# Exclude Plasticity Index values with a count of 0 (though `value_counts` should not include zero counts)
count_data = count_data[count_data['Count'] > 0]

# Sort by Plasticity Index value
count_data = count_data.sort_values(by='PlasticityIndex')

# Display the DataFrame
st.write("Plasticity Index Count Data:")
st.write(count_data)

# Prepare data for echarts
x_data = count_data['PlasticityIndex'].astype(str).tolist()  # Use strings for x-axis labels
y_data = count_data['Count'].tolist()

# Echarts options for a line graph
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
            "type": "line",  # Line chart type
            "data": y_data
        }
    ]
}

# Render the chart with Streamlit
st.subheader("Plasticity Index vs. Count of Samples for OADBY TILL MEMBER")

st_echarts(options=chart_options)
