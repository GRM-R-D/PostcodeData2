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

# Exclude Plasticity Index values with a count of 0 (though `value_counts` should not include zero counts)
count_data = count_data[count_data['Count'] > 0]

# Sort by Plasticity Index value
count_data = count_data.sort_values(by='PlasticityIndex')

# Display the DataFrame
st.write("Plasticity Index Count Data:")
st.write(count_data)

# Prepare the Plotly Express line chart with Count on x-axis and PlasticityIndex on y-axis
fig = px.line(count_data, x='Count', y='PlasticityIndex',
              title='Count of Samples vs. Plasticity Index',
              labels={'Count': 'Count of Samples', 'PlasticityIndex': 'Plasticity Index'})

# Customize the chart
fig.update_layout(
    xaxis_title='Count of Samples',
    yaxis_title='Plasticity Index',
    title=dict(text='Count of Samples vs. Plasticity Index', x=0.5),
    yaxis=dict(tickmode='linear')  # Ensure y-axis shows linear scale
)

# Render the chart with Streamlit
st.subheader("Count of Samples vs. Plasticity Index for OADBY TILL MEMBER")
st.plotly_chart(fig, use_container_width=True)
