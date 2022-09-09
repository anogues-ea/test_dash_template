from dash_extensions.enrich import Output, Input, State, html, callback, register_page, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# This is needed to add the page to navigation
# You can remove order if you don't care about page ordering in navbar
register_page(
    __name__,
    path='/complex_page',
    title='Complex page',
    name='Complex page',
    order=2
)


# the page needs to contain either a function called layout returning the layout or a layout object
def layout():
    # store data in local cache
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    storage = dcc.Store(id='df-storage', storage_type='memory', data=df.to_dict(orient='records')),

    # create page elements
    slider = dcc.RangeSlider(df['year'].min(), df['year'].max(), step=None, value=[df['year'].min(), df['year'].max()],
                             marks={str(year): str(year) for year in df['year'].unique()}, id='year-slider')
    graph = dcc.Graph(id='graph-with-slider')
    table = dash_table.DataTable(id='table-with-slider', style_table={'overflowX': 'auto', 'overflowY': 'auto'})

    # add elements to layout
    layout = html.Div([
        dbc.Row(storage),
        dbc.Row(
            [dbc.Col(html.Div(children=[graph, slider])),
             # constrain the size of the table to 80% of monitor height, make it scrollable
             dbc.Col(html.Div(children=[table], style={'max-height': '80vh', 'overflow': 'auto'}))
             ]
        )
    ])
    return layout


@callback(
    Output('graph-with-slider', 'figure'),
    Output('table-with-slider', 'columns'),
    Output('table-with-slider', 'data'),
    Input('year-slider', 'value'),
    State('df-storage', 'data')
)
def update_figures(selected_years, df_json):
    # read cached data
    df = pd.DataFrame(df_json)
    filtered_df = df[(df.year >= selected_years[0]) & (df.year <= selected_years[1])]

    # make figure
    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)
    fig.update_layout(transition_duration=500)

    # make table
    columns = [{"name": i, "id": i} for i in filtered_df.columns]
    data = filtered_df.to_dict('records')

    return fig, columns, data
