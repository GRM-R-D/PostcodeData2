import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Display the data (optional)
st.write("Data from CSV:")
st.write(data)

# Create the line chart using Altair for more customization
chart = alt.Chart(data).mark_line().encode(
    x='Date:T',
    y='PlasticityIndex:Q'
).properties(
    title='Plasticity Index Over Time',
    width=700,
    height=400
)

# Display the chart in Streamlit as a Vega-Lite chart
st.vega_lite_chart(chart, use_container_width=True)
