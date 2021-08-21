from pandas.core  import groupby
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data.csv')

print(df.loc[df["student_id"]=="TRL_xyz"])
student_df = df.loc[df["student_id"]=="TRL_xyz"]
figure = go.Figure(go.Bar(x=student_df.groupby("level")["attempt"].mean(),y=["Level 1", "Level 2","Level 3","Level 4"],orientation="h"))

figure.show()