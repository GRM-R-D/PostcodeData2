import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Display the data (optional)
st.write("Data from CSV:")
st.write(data)

# Create the line chart
st.line_chart(data)

# If you want to customize the x and y axes, you can specify the columns
# For example, if your CSV has columns 'Date' and 'Value'
# st.line_chart(data.set_index('Date')['Value'])
