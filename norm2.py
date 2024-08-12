import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the CSV data
data = pd.read_csv('Pointdate.csv')

# Ensure 'Date' is a datetime column
data['Date'] = pd.to_datetime(data['Date'])

# Filter data to include only rows with the specified geology
filtered_data = data[data['GeologyCode'] == 'OADBY TILL MEMBER']

# Calculate the mean Plasticity Index for each Date
mean_data = filtered_data.groupby('Date', as_index=False)['PlasticityIndex'].mean()

# Z-Score Normalization
scaler = StandardScaler()
mean_data[['PlasticityIndex']] = scaler.fit_transform(mean_data[['PlasticityIndex']])

# Display normalized data
print(mean_data.head())
