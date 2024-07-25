from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
from Home import add_logo

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Custom Data Visualisation by attributes",
    layout="wide"
)

logo_url = "https://grmdevelopment.wpengine.com/wp-content/uploads/2020/07/GRM-master-logo-02.png"
# Call add_logo function from Home module with default logo_url
add_logo(logo_url, height=100)

# Import your data
df = pd.read_csv("Points.csv")

pyg_app = StreamlitRenderer(df)

pyg_app.explorer()
