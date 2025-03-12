import dash
from dash import dcc, html
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data
df = px.data.gapminder().query("country == 'India'")

# Create a Plotly figure
fig = px.line(df, x='year', y='gdpPercap', title="India's GDP Over Time")

# Layout of the app
app.layout = html.Div([
    html.H1("Simple Dash App"),
    dcc.Graph(id='line-chart', figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
