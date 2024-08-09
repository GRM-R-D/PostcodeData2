import streamlit as st
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

st.bar_chart(data.set_index('Category'))
