import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

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

# Create ECharts line chart specification
chart_options = {
    'title': {
        'text': 'Mean Plasticity Index Over Time for OADBY TILL MEMBER',
        'left': 'center'
    },
    'tooltip': {
        'trigger': 'axis'
    },
    'xAxis': {
        'type': 'time',
        'name': 'Date',
        'nameLocation': 'middle',
        'nameGap': 30
    },
    'yAxis': {
        'type': 'value',
        'name': 'Mean Plasticity Index',
        'nameLocation': 'middle',
        'nameGap': 50
    },
    'series': [{
        'data': [[int(pd.Timestamp(d).timestamp() * 1000), pi] for d, pi in mean_data[['Date', 'PlasticityIndex']].values],
        'type': 'line',
        'smooth': True,
        'areaStyle': {}
    }],
    'dataZoom': [{
        'type': 'inside'
    }]
}

# Display the ECharts chart in Streamlit
st_echarts(options=chart_options, height='400px')