import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file

df = pd.read_csv("data.csv")

df["Value"] = df["Value"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)
df["Wage"] = df["Wage"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)

df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df["Wage"] = pd.to_numeric(df["Wage"], errors="coerce")

df_plot = df[["Name", "Wage", "Value"]].dropna()

source = ColumnDataSource(df_plot)

output_file("grafic_jucatori.html")

p = figure(
    title="Relatia dintre Wage si Value",
    x_axis_label="Wage",
    y_axis_label="Value",
    width=900,
    height=600,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

p.circle("Wage", "Value", size=8, source=source)

hover = HoverTool(tooltips=[
    ("Jucator", "@Name"),
    ("Wage", "@Wage"),
    ("Value", "@Value")
])

p.add_tools(hover)

show(p)