import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import line_chart

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

# Create Lightweight Charts line chart
line_chart(
    chart_data,
    x='x',
    y='y',
    title='Plasticity Index vs Count of OADBY TILL MEMBER',
    line_color='blue',
    line_width=2,
    x_axis_label='Plasticity Index',
    y_axis_label='Count'
)
