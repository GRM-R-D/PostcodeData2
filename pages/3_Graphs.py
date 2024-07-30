from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('Pointdate.csv')
AgGrid(df)