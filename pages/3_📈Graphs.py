import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from statsmodels.nonparametric.smoothers_lowess import lowess

# Set up the Streamlit page
st.set_page_config(page_title="Graphs", page_icon="📈", layout="wide")

@st.cache_resource
def add_logo(logo_url: str, width: int = 250, height: int = 300):
    """Add a logo (from logo_url) on the top of the navigation page of a multipage app."""
    logo_css = f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url({logo_url});
                background-repeat: no-repeat;
                background-size: {width}px {height}px; /* Set the size of the logo */
                padding-top: {height + 20}px;
                background-position: 20px 0px;
            }}
        </style>
    """
    st.markdown(logo_css, unsafe_allow_html=True)


# Add a markdown header
st.markdown("## Trends Graphs")

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column (if you have date-related features)
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'GLACIAL DEPOSITS']

# Count the number of samples for each Plasticity Index value
count_data = filtered_data['PlasticityIndex'].value_counts().reset_index()
count_data.columns = ['PlasticityIndex', 'Count of Samples']

# Exclude Plasticity Index values that are 0
count_data = count_data[count_data['PlasticityIndex'] != 0]

# Sort by Plasticity Index value
count_data = count_data.sort_values(by='PlasticityIndex')

# Compute LOWESS trendline
lowess_result = lowess(count_data['Count of Samples'], count_data['PlasticityIndex'], frac=0.2)
x_lowess = lowess_result[:, 0]
y_lowess = lowess_result[:, 1]

# Create a scatter plot with LOWESS trendline
fig = go.Figure()

# Add scatter points
fig.add_trace(go.Scatter(x=count_data['PlasticityIndex'], y=count_data['Count of Samples'],
                         mode='markers', name='Sample Points'))

# Add LOWESS trendline
fig.add_trace(go.Scatter(x=x_lowess, y=y_lowess,
                         mode='lines', name='LOWESS Trendline'))

# Customize the chart
fig.update_layout(
    xaxis_title='Plasticity Index',
    yaxis_title='Count of Samples',
    title=dict(text='Plasticity Index vs. Count of Samples with Trendline', x=0.5),
    xaxis=dict(
        tickmode='linear',
        dtick=5  # Set the increment of x-axis ticks. Change this value to adjust increments.
    )
)

# Create a two-column layout
col1, col2 = st.columns([1, 2])  # Adjust column widths as needed

with col1:
    st.write("Plasticity Index Count Data:")
    st.dataframe(count_data, hide_index=True)

with col2:
    st.subheader("Plasticity Index vs. Count of Samples for GLACIAL DEPOSITS")
    st.plotly_chart(fig, use_container_width=True)
