import uuid

import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from Layouts.PageHeader import page_header
from Layouts.PageContent import page_content_form
from DataModel.DataReader import DataReader
from DataModel.QueryGenerator import QueryGenerator
from Predict import Predict
from dash.dependencies import Input, Output, State
from datetime import date

from Layouts.ValidationAlerts import page_validations

main = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
main.title = "Health Insurance Customer Details"


def serve_layout():
    session_id = str(uuid.uuid4())
    return html.Div([
        dcc.Store(data=session_id, id='session_id'),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])


main.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    page_header,
    page_validations,
    page_content_form,
    dcc.Store(id='intermediate-value')
])

data_read_obj = DataReader()
query_generator_obj = QueryGenerator()
model_prediction_obj = Predict()


@main.callback(
    Output('input-Region', 'options'),
    Input('input-Region', 'options')
)
def region_code(code):
    sql_query_read_region_code = query_generator_obj.create_select_query('policyholders_db', 'region_code',
                                                                         ['Region_Code'])
    region_code_id = data_read_obj.read_data(sql_query_read_region_code)

    region_code_list = []
    for i in range(0, 53):
        region = {"label": region_code_id[i][0], "value": region_code_id[i][0]}
        region_code_list.append(region)

    return region_code_list


@main.callback(
    Output('input-Policy-Sales-Channel', 'options'),
    Input('input-Policy-Sales-Channel', 'options')
)
def policy_sales_channel_code(channel):
    sql_query_read_sales_channel = query_generator_obj.create_select_query('policyholders_db', 'policy_sales_channel',
                                                                           ['Policy_Sales_Channel'])
    sales_channel_code = data_read_obj.read_data(sql_query_read_sales_channel)

    sales_channel_code_list = []
    for i in range(0, 155):
        sales_channel = {"label": sales_channel_code[i][0], "value": sales_channel_code[i][0]}
        sales_channel_code_list.append(sales_channel)

    return sales_channel_code_list


@main.callback(
    Output('success-confirmation', 'is_open'),
    Input('process-button', 'n_clicks')
)
def process_all(n_clicks):
    if n_clicks > 0:
        sql_query_read_region_code = query_generator_obj.create_select_query('policyholders_db', 'policyholders_data',
                                                                             ['*'])
        region_code_id = data_read_obj.read_data(sql_query_read_region_code)
        today = date.today()
        for i in region_code_id:
            print(model_prediction_obj.data_prediction(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                                                       (today - i[10]).days))
        return True
    return False


@main.callback(
    Output("url", "href"),
    Input('close-button', 'n_clicks'),
    prevent_initial_call=True,
)
def reset(close_button_clicks):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if close_button_clicks > 0:
        if ctx.triggered:
            if button_id == "close-button":
                return "/"


if __name__ == "__main__":
    main.run_server(debug=True)
