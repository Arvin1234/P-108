import plotly.figure_factory as ff
import csv
import pandas as pd
df = pd.read_csv("data1.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Rating"], show_hist = False)
fig.show()