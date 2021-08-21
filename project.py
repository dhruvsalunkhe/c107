import pandas as pd
from pandas.core import groupby
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('data.csv')

print(df.groupby(["student_id","level"],as_index=False)["attempt"].mean())
mean = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
figure = px.scatter(mean,x = "student_id", y = "level", size = "attempt", color="attempt")

figure.show()