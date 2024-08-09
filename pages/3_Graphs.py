import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

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

# Prepare data for Highcharts
x_data = count_data['PlasticityIndex'].astype(str).tolist()  # Use strings for x-axis labels
y_data = count_data['Count'].tolist()

# Highcharts options for a line graph
chart_options = {
    "title": {
        "text": "Plasticity Index vs. Count of Samples",
        "subtext": "For OADBY TILL MEMBER"
    },
    "tooltip": {
        "shared": True,
        "crosshairs": True
    },
    "xAxis": {
        "categories": x_data,
        "title": {
            "text": "Plasticity Index"
        }
    },
    "yAxis": {
        "title": {
            "text": "Count of Samples"
        }
    },
    "series": [{
        "name": "Count of Samples",
        "data": y_data,
        "type": "line"  # Line chart type
    }]
}

# Create a Highcharts component
highcharts_component = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Highcharts Example</title>
    <script src="https://code.highcharts.com/highcharts.js"></script>
</head>
<body>
    <div id="container" style="width: 100%; height: 400px;"></div>
    <script>
        Highcharts.chart('container', {chart_options});
    </script>
</body>
</html>
"""

# Render the Highcharts component with Streamlit
st.subheader("Plasticity Index vs. Count of Samples for OADBY TILL MEMBER")
components.html(highcharts_component, height=400)
