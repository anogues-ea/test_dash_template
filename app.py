from dash_extensions.enrich import DashProxy,  MultiplexerTransform
import dash_bootstrap_components as dbc

import dash
from templates.master_template import make_master_template

app = DashProxy(transforms=[MultiplexerTransform()], use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = make_master_template(page_registry=dash.page_registry, page_container=dash.page_container)

if __name__ == '__main__':
	app.run_server(debug=True)