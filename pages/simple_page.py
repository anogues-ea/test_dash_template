from dash_extensions.enrich import html, register_page, dcc
import plotly.express as px
import pandas as pd

# This is needed to add the page to navigation
# You can remove order if you don't care about page ordering in navbar
register_page(
    __name__,
    path='/simple_page',
    title='Simple page',
    name='Simple page',
    order=1
)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# the page needs to contain either a function called layout returning the layout or a layout object
layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
