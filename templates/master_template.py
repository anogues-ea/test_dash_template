import dash_bootstrap_components as dbc
from dash_extensions.enrich import html


def make_navbar(page_registry):
    nav_pages = [dbc.DropdownMenuItem(f"{page['name']}", href=page["relative_path"])
                 for page in page_registry.values()]
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                children=nav_pages,
                nav=True,
                in_navbar=True,
                label="Pages",
            ),
        ],
        brand="App name",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar


def make_master_template(page_registry, page_container):
    layout = []
    # add navbar
    layout.append(
        dbc.Row(
            dbc.Col(
                make_navbar(page_registry)
            ))
    )
    # add page container
    layout.append(page_container)

    return html.Div(layout)
