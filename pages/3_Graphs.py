import streamlit as st
from bokeh.plotting import figure

# Create a simple plot
p = figure(title="Simple Example", x_axis_label="x", y_axis_label="y")
p.line([1, 2, 3], [4, 5, 6])

# Display the plot
st.bokeh_chart(p, use_container_width=True)