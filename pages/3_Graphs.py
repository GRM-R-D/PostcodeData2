import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource

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

# Prepare data for Bokeh
x_data = count_data['PlasticityIndex'].astype(str).tolist()  # Use strings for x-axis labels
y_data = count_data['Count'].tolist()

# Create a Bokeh plot
p = figure(title="Plasticity Index vs. Count of Samples",
           x_axis_label='Plasticity Index',
           y_axis_label='Count',
           x_range=x_data,  # Use x_data for categorical x-axis
           plot_height=400,
           plot_width=700,
           tools="")

# Add a line renderer with legend and line thickness
p.line(x_data, y_data, legend_label="Count of Samples", line_width=2, color='blue')

# Add circle markers
p.circle(x_data, y_data, size=8, color='red', alpha=0.6)

# Show grid lines on both axes
p.grid.grid_line_color = 'gray'
p.grid.grid_line_alpha = 0.5

# Render the Bokeh plot with Streamlit
st.subheader("Plasticity Index vs. Count of Samples for OADBY TILL MEMBER")
st.bokeh_chart(p)
