import plotly.express as px
import pandas as pd


# Import data from GitHub
data = pd.read_csv(
    "gas-prices.csv"
)

# Create basic choropleth map
fig = px.choropleth(
    data,
    locations="iso_alpha",
    color="ppl",
    hover_name="country",
    projection="natural earth",
    animation_frame="year",
    title="Gas Prices by Country",
)
fig.show()
