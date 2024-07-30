import streamlit as st
import pandas as pd
import numpy as np

DataFrame = 'Pointdate.csv'

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Date", "PlasticityIndex"])

st.line_chart(chart_data)