import dash
from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3],
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Fruit Visualization Dashboard'),
    dcc.Dropdown(
        id="fruit-dropdown",
        options=[{'label': fruit, 'value': fruit} for fruit in df['Fruit']],
        # value='Apples',
        placeholder="Select a Fruit",
        clearable=False,
    ),
    dcc.Graph(id="fruit-graph"),
])

# Define the callback to update the graph
@app.callback(
    Output("fruit-graph", "figure"), 
    Input("fruit-dropdown", 'value'))        
def update_graph(selected_fruit):
    # df = pd.DataFrame(data)
    # mask = df["Fruit"] == selected_fruit

    # Filter data based on selected fruit
    filtered_df = df[df['Fruit'] == selected_fruit]

    # Create a bar chart
    fig = px.bar(filtered_df, x='Fruit', y='Amount', title=f"Amount of {selected_fruit}")

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)