# dash_apps_template
Template for Dash app

## Getting Started

* clone repo by clicking on "use this template" from github.
* clone new repo locally.
* checkout develop branch.
* Install requirements in conda / venv
* run app.py to start the app
## TLDR
### 1/ Edit navbar parameters
* Go to src/templates/master_template.py
* Edit brand to change app name

### 2/ Choose a theme
* Go to src/app.py
* Pick a theme from https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
* Update external_stylesheets=[dbc.themes.BOOTSTRAP]

### 3/Create new pages
* Add pages to src/pages following example pages
* Include the register_page function to add the page to navigation (like in examples)
* Have either a layout object or a function called layout returning a layout
* Import components using from dash_extensions.enrich import foor, bar instead of from dash import foo, bar
* Build the page as a normal Dash page


## Included in the template

### Standard layout and navigation bar
#### Usage
The template is built around a multi-page app navigated through a top navigation bar.<br>
The navigation bar can be found in:<br>
src/templates/master_template.py
The following parameters can be edited to personalise the app

~~~python
def make_navbar(page_registry):
        ...
        brand="App name",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar
~~~

You do not have to touch anything else. <br>
New pages will automatically be added to navigation, boostrap themes will be automatically added to elements.



### Dash multi page support
Dash is by default a single page application framework.<br>
However, a multi page solution (previously part of dash-extensions and now part of Dash base package) <br>
is pre implemented in this template.
#### Documentation
https://dash.plotly.com/urls
#### Usage
To create a new page, create a file in the pages directory.<br>

The page should have at least these 2 components:
##### A register page call
```python
from dash_extensions.enrich import register_page

register_page(
    __name__,
    path='/',
    title='Home',
    name='Home',
    order=0
)
```
This registers the page in the dash page_registry. <br>
We use the page_registry to add links to navigation bar and map links to page layouts and callbacks
##### A layout object or function
The page needs to have either a layout object:
```python
layout = html.Div(children=[html.H1(children='Hello Dash')])

```
or a function called layout returning a layout
```python
def layout():
    layout = html.Div(children=[html.H1(children='Hello Dash')])
    return layout
```
Create your page as usual with layout and callbacks.<br>
As long as the register_page function is called, the page will be added to the navigation bar and will work.<br>
If you want to control the order in which pages appear in the navbar, use the order argument of register_page.<br>
It can be removed if not used.

### Multiplexer (multiple callbacks for single output)
The base Dash package prevents multiple callbacks from having their output pointing to a single object.<br>
This causes issues when creating load / iterate workflows in which an object might be initially loaded then <br> 
updated using different callbacks. <br>
This is addressed by the dash-extensions package <br>
Note that dash-extensions multiplexer affects how loaders and callbacks operations like Match work.<br>
Please read documentations for solutions.

The multiplexer is implemented by replacing the normal app creation workflow
```python
app = DashProxy(transforms=[MultiplexerTransform()], use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
```
Instead of
```python
app = Dash(__name__)
```
Keep this into account when trying to do fancy things like exposing the underlying flask server...<br>
your app is no longer the standard Dash object.

#### Documentation and packages
https://pypi.org/project/dash-extensions/ <br>
https://www.dash-extensions.com/pages/transforms/multiplexer-transform
#### Usage
When creating layouts and callbacks, instead of working with normal Dash components:
```python
from dash import Output, Input, html, dcc

@callback(
    Output('example-graph', 'figure'),
    Input('button-1', 'n_clicks'))
def update_figures(selected_years, df_json):
    ...
    return fig
```

Follow the same workflow but with importing components from dash-extensions

```python
from dash_extensions.enrich  import Output, Input, html, dcc

@callback(
    Output('example-graph', 'figure'),
    Input('button-1', 'n_clicks'))
def update_figures(selected_years, df_json):
    ...
    return fig
```
You should be able to create multiple callbacks pointing at the same object.


### Dash bootstrap
Dash bootstrap brings additional elements to Dash making apps more interactive and better looking. <br>
It also comes with a number of themes to be used as stylesheets. <br>

#### Documentation
https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/
#### Usage
##### Stylesheets
Stylesheets are passed to the app in app.py here:
```commandline
import dash_bootstrap_components as dbc
app = DashProxy(external_stylesheets=[dbc.themes.BOOTSTRAP])
```
You can  choose a style at: <br>
https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
##### Layout and elements
You can use dash bootstrap instead of built in CSS tools to create layouts. <br>
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

You can also use some Bootstrap elements in your Dash app to make it more dynamic: <br>
For example, I like using modals to make 'popup' tables to complement charts.<br>
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/modal/



