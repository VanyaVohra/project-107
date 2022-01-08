import csv
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")

studentDF = df.loc[df["student_id"] == "TRL_987"]

print(studentDF.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = studentDF.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "h"
))

fig.show()

#print(studentDF)
#print(df)