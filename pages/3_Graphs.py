import streamlit as st
import pandas as pd
import altair as alt

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

# Create the line chart using Altair with smooth interpolation for more customization
chart = alt.Chart(mean_data).mark_line(interpolate='monotone').encode(
    x='Date:T',
    y='PlasticityIndex:Q'
).properties(
    title='Mean Plasticity Index Over Time for OADBY TILL MEMBER',
    width=700,
    height=400
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)
