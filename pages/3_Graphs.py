import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Count the occurrences of 'OADBY TILL MEMBER' and list Plasticity Index values
count_data = filtered_data.groupby('PlasticityIndex').size().reset_index(name='Count')

# Display the filtered data (optional)
st.write("Count Data:")
st.write(count_data)

# Create ECharts line chart specification
chart_options = {
    'title': {
        'text': 'Plasticity Index vs Count of OADBY TILL MEMBER',
        'left': 'center'
    },
    'tooltip': {
        'trigger': 'axis'
    },
    'xAxis': {
        'type': 'value',
        'name': 'Count',
        'nameLocation': 'middle',
        'nameGap': 30
    },
    'yAxis': {
        'type': 'value',
        'name': 'Plasticity Index',
        'nameLocation': 'middle',
        'nameGap': 50
    },
    'series': [{
        'data': count_data[['Count', 'PlasticityIndex']].values.tolist(),
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
