from dash_extensions.enrich import html, register_page

# This is needed to add the page to navigation
# You can remove order if you don't care about page ordering in navbar
register_page(
    __name__,
    path='/',
    title='Home',
    name='Home',
    order=0
)

# the page needs to contain either a function called layout returning the layout or a layout object
layout = html.Div(children=[
    html.H1(children='This is our Home page'),
    html.Div(children='''
        This is our Home page content.
    '''),

])