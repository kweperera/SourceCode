from dash import dcc
import dash_bootstrap_components as dbc
from dash import html

# Main form inputs
title_input = dbc.FormGroup(
    [
        dbc.Label("Title", html_for="input-Title", width=2),
        dbc.Col(
            dcc.Dropdown(id='input-Title',
                         options=[
                             {"label": "Mr.", "value": "Mr."},
                             {"label": "Mrs.", "value": "Mrs."},
                             {"label": "Miss.", "value": "Miss."},
                             {"label": "Dr.", "value": "Dr."}
                         ]),
            width=6,
        ),
    ],
    row=True
)

name_input = dbc.FormGroup(
    [
        dbc.Label("Full Name", html_for="input-Name", width=2),
        dbc.Col(
            dbc.Input(id='input-Name', type='text', placeholder='Enter Full Name'),
            width=6,
        ),
    ],
    row=True
)

email_input = dbc.FormGroup(
    [
        dbc.Label("Email", html_for="input-Email", width=2),
        dbc.Col(
            dbc.Input(id='input-Email', type='email', placeholder='Enter Email'),
            width=6,
        ),
    ],
    row=True
)

contact_input = dbc.FormGroup(
    [
        dbc.Label("Contact Number", html_for="input-Contact", width=2),
        dbc.Col(
            dbc.Input(id='input-Contact', type='text', placeholder='Enter Contact Number'),
            width=6,
        ),
    ],
    row=True
)

gender_input = dbc.FormGroup(
    [
        dbc.Label("Gender", html_for="input-Gender", width=2),
        dbc.Col(
            dcc.Dropdown(id='input-Gender',
                         options=[
                             {"label": "Male", "value": "Male"},
                             {"label": "Female", "value": "Female"}
                         ]),
            width=6,
        ),
    ],
    row=True
)

age_input = dbc.FormGroup(
    [
        dbc.Label("Age", html_for="input-Age", width=2),
        dbc.Col(
            dbc.Input(id='input-Age', type='number', min=18, max=90, placeholder='Enter Age'),
            width=6,
        ),
    ],
    row=True
)

annual_premium_input = dbc.FormGroup(
    [
        dbc.Label("Annual Premium", html_for="input-Annual-Premium", width=2),
        dbc.Col(
            dbc.Input(id='input-Annual-Premium', type='number', min=0, placeholder='Enter Annual Premium'),
            width=6,
        ),
    ],
    row=True
)

policy_sales_channel_input = dbc.FormGroup(
    [
        dbc.Label("Policy Sales Channel", html_for="input-Policy-Sales-Channel", width=2),
        dbc.Col(
            dcc.Dropdown(id='input-Policy-Sales-Channel'),
            width=6,
        ),
    ],
    row=True
)

region_input = dbc.FormGroup(
    [
        dbc.Label("Region Code", html_for="input-Region", width=2),
        dbc.Col(
            dcc.Dropdown(id='input-Region'),
            width=6,
        ),
    ],
    row=True
)

driving_license_input = dbc.FormGroup(
    [
        dbc.Label("Do you have a driving license?", html_for="input-Driving-License", width=2),
        dbc.Col(
            dbc.RadioItems(id='input-Driving-License',
                           options=[
                               {"label": "Yes", "value": "1"},
                               {"label": "No", "value": "0"}
                           ]),
            width=6,
        ),
    ],
    row=True
)

vehicle_insurance_input = dbc.FormGroup(
    [
        dbc.Label("Do you have a vehicle insurance?", html_for="input-Vehicle-Insurance", width=2),
        dbc.Col(
            dbc.RadioItems(id='input-Vehicle-Insurance',
                           options=[
                               {"label": "Yes", "value": "1"},
                               {"label": "No", "value": "0"}
                           ]),
            width=6,
        ),
    ],
    row=True
)

vehicle_age_input = dbc.FormGroup(
    [
        dbc.Label("Vehicle Age", html_for="input-Vehicle-Age", width=2),
        dbc.Col(
            dcc.Dropdown(id='input-Vehicle-Age',
                         options=[
                             {"label": "< 1 Year", "value": "< 1 Year"},
                             {"label": "1-2 Year", "value": "1-2 Year"},
                             {"label": "> 2 Years", "value": "> 2 Years"}
                         ]),
            width=6,
        ),
    ],
    row=True
)

vehicle_damage_input = dbc.FormGroup(
    [
        dbc.Label("Did your vehicle get damaged in the past?", html_for="input-Vehicle-Damage", width=2),
        dbc.Col(
            dbc.RadioItems(id='input-Vehicle-Damage',
                           options=[
                               {"label": "Yes", "value": "Yes"},
                               {"label": "No", "value": "No"}
                           ]),
            width=6,
        ),
    ],
    row=True
)

annual_premium_input = dbc.FormGroup(
    [
        dbc.Label("Annual Premium", html_for="input-Annual-Premium", width=2),
        dbc.Col(
            dbc.Input(id='input-Annual-Premium', type='number', min=0, placeholder='Enter Annual Premium'),
            width=6,
        ),
    ],
    row=True
)

page_content_form = html.Div(
    className="app-form",
    children=[dbc.Form(
        [title_input, name_input, email_input, contact_input, age_input, gender_input,
         annual_premium_input, policy_sales_channel_input, region_input, driving_license_input,
         vehicle_insurance_input, vehicle_age_input, vehicle_damage_input]),

        html.Div(
            className="app-button",
            children=dbc.Button(id='process-button', n_clicks=0, children='process all',
                                className="mr-1")
        )
    ],

)
