import streamlit as st
import pandas as pd

st.set_page_config(page_title="Postcode Data", page_icon="📈")

st.markdown("# Postcode Data")
st.sidebar.header("Postcode Data")
st.write(
    """This page shows a table of UK postcodes and their corresponding Atterberg Limits"""
)

# Load the CSV file from the data subfolder
filename = 'postcodes.csv'  # replace with your actual CSV file path
df = pd.read_csv(filename)

# Drop the 'fid' column if it exists
if 'fid' in df.columns:
    df = df.drop(columns=['fid'])

# Rename columns
df = df.rename(columns={'name': 'Postcode', 'AVG PL_mea': 'Average PL', 'AVG LL_mea': 'Average LL', 'AVG INDEX_': 'Average PI', 'AVG MC_mea': 'Average MC'})

# Filter out rows with None in any column
df_filtered = df.dropna()

# Display the filtered data table without the index
st.dataframe(
            df_filtered,
            column_config={
            "Postcode": st.column_config.Column(
            width="small"
            ),
            "Average PL": st.column_config.Column(
            width="small"
            ),
            "Average LL": st.column_config.Column(
            width="small"
            ),
            "Average PI": st.column_config.Column(
            width="small"
            ),
            "Average MC": st.column_config.Column(
            width="small"
            ),
        },
        width=800, hide_index=True)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
