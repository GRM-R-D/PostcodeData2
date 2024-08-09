import streamlit as st
import pandas as pd
import streamlit_highcharts as hg

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column (if you have date-related features)
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Count the number of samples for each Plasticity Index value
count_data = filtered_data['PlasticityIndex'].value_counts().reset_index()
count_data.columns = ['PlasticityIndex', 'Count']

# Exclude Plasticity Index values with a count of 0 (though value_counts should not include zero counts)
count_data = count_data[count_data['Count'] > 0]

# Sort by Plasticity Index value
count_data = count_data.sort_values(by='PlasticityIndex')

# Prepare data for Highcharts
x_data = count_data['PlasticityIndex'].tolist()  # Numeric x-values
y_data = count_data['Count'].tolist()

# Highcharts options for a spline graph with numeric x-axis
chart_options = {
    'chart': {
        'type': 'spline',
        'zoomType': 'x',
    },
    'title': {
        'text': 'Plasticity Index vs. Count of Samples for OADBY TILL MEMBER',
        'align': 'center'
    },
    'xAxis': {
        'type': 'linear',  # Use 'linear' for numeric x-axis
        'title': {
            'text': 'Plasticity Index'
        }
    },
    'yAxis': {
        'title': {
            'text': 'Count of Samples'
        }
    },
    'series': [{
        'name': 'Count of Samples',
        'data': list(zip(x_data, y_data)),  # Combine x and y data into tuples
        'lineWidth': 2,
        'color': '#FF5733',
        'marker': {
            'enabled': False
        },
        'fillOpacity': 0.3
    }],
    'plotOptions': {
        'spline': {
            'marker': {
                'enabled': False
            },
        }
    }
}

# Render the chart with Streamlit
st.subheader("Plasticity Index vs. Count of Samples for OADBY TILL MEMBER")
hg.Highcharts(options=chart_options)
