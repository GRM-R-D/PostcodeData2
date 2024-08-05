import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Display the data (optional)
st.write("Data from CSV:")
st.write(data)

# Create the line chart using Streamlit's st.line_chart
st.line_chart(data.set_index('Date')['PlasticityIndex'])
