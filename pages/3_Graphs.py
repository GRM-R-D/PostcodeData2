import pandas as pd
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

# Step 1: Read the CSV file
csv_file = 'Pointdate.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Assuming your CSV has columns 'Date' and 'PlasticityIndex'
x_data = df['Date'].tolist()
y_data = df['PlasticityIndex'].tolist()

# Prepare the chart data in the format required by lightweight charts
chart_data = [{"time": x, "value": y} for x, y in zip(x_data, y_data)]

# Define the chart configuration
chart_config = {
    "width": 600,
    "height": 400,
    "series": [
        {
            "type": "Line",
            "data": chart_data,
            "options": {"color": "blue"}
        }
    ],
    "options": {
        "priceScale": {"mode": 1},
        "timeScale": {
            "timeVisible": True,
            "secondsVisible": False,
        },
        "crossHair": {
            "mode": 1,
        },
        "grid": {
            "vertLines": {"color": "#ebebeb"},
            "horzLines": {"color": "#ebebeb"},
        },
    },
}

# Step 2: Render the chart in Streamlit
renderLightweightCharts([chart_config], key="line_chart")
