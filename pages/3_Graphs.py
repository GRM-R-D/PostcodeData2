import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column (if you have date-related features)
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Count the number of samples for each Plasticity Index value
count_data = filtered_data['PlasticityIndex'].value_counts().reset_index()
count_data.columns = ['PlasticityIndex', 'Count']

# Exclude Plasticity Index values that are 0
count_data = count_data[count_data['PlasticityIndex'] != 0]

# Sort by Plasticity Index value
count_data = count_data.sort_values(by='PlasticityIndex')

# Display the DataFrame
st.write("Plasticity Index Count Data:")
st.write(count_data)

# Prepare the Plotly Express line chart
fig = px.line(count_data, x='PlasticityIndex', y='Count',
              title='Plasticity Index vs. Count of Samples',
              labels={'PlasticityIndex': 'Plasticity Index', 'Count': 'Count of Samples'})

# Customize the chart
fig.update_layout(
    xaxis_title='Plasticity Index',
    yaxis_title='Count of Samples',
    title=dict(text='Plasticity Index vs. Count of Samples', x=0.5),
    xaxis=dict(
        tickmode='linear',
        dtick=5  # Set the increment of x-axis ticks. Change this value to adjust increments.
    )
)

# Render the chart with Streamlit
st.subheader("Plasticity Index vs. Count of Samples for OADBY TILL MEMBER")
st.plotly_chart(fig, use_container_width=True)
