import streamlit as st
import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'x': ['A', 'B', 'C', 'D'],
    'y': [5, 10, 15, 20]
})

# Create chart
chart = alt.Chart(data).mark_bar().encode(
    x='x:O',
    y='y:Q'
)

st.altair_chart(chart, use_container_width=True)
