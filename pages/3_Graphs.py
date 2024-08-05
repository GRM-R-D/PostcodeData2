import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

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

# Prepare data for streamlit-lightweight-charts
chart_data = mean_data[['Date', 'PlasticityIndex']].rename(columns={'Date': 'time', 'PlasticityIndex': 'value'})

# Display the chart in Streamlit using streamlit-lightweight-charts
st.line_chart(chart_data, x='time', y='value', title='Mean Plasticity Index Over Time for OADBY TILL MEMBER', width=700, height=400)