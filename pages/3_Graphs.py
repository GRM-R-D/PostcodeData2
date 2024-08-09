import streamlit as st
import pandas as pd
from streamlit_google_charts import google_chart

# Sample Data
pop_data = [
    ['City', '2010 Population', '2000 Population'],
    ['New York City, NY', 8175000, 8008000],
    ['Los Angeles, CA', 3792000, 3694000],
    ['Chicago, IL', 2695000, 2896000],
    ['Houston, TX', 2099000, 1953000],
    ['Philadelphia, PA', 1526000, 1517000],
]

# Streamlit app
st.title('Google Charts with Streamlit')
st.subheader("Bar Chart Demo")

# Prepare data for Google Charts
chart_data = [['City', '2010 Population', '2000 Population']] + pop_data[1:]

# Google Charts configuration
chart_options = {
    'title': 'Population of Largest U.S. Cities',
    'hAxis': {'title': 'Total Population', 'minValue': 0},
    'vAxis': {'title': 'City'},
    'width': 500,
    'height': 300,
}

# Display the chart
google_chart(data=chart_data, chartType='BarChart', options=chart_options)
