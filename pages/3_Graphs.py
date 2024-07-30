import pandas as pd
from streamlit_echarts import st_echarts

# Step 1: Read the CSV file
csv_file = 'Pointdate.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Assuming your CSV has columns 'Date' and 'PlasticityIndex'
x_data = df['Date'].tolist()
y_data = df['PlasticityIndex'].tolist()

# Step 2: Create the options dictionary for ECharts
options = {
    "title": {
        "text": "Plasticity Index over Time",
        "subtext": "Data from Pointdate.csv"
    },
    "toolbox": {
        "show": True
    },
    "xAxis": {
        "type": "category",
        "data": x_data
    },
    "yAxis": {
        "type": "value"
    },
    "series": [{
        "data": y_data,
        "type": "bar",
        "name": "Plasticity Index"
    }]
}

# Step 3: Display the chart in Streamlit
st_echarts(options=options)
