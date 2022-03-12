import dash_bootstrap_components as dbc
import dash_html_components as html


page_validations = html.Div(
    children=[
        # Transaction confirmation
        dbc.Modal(
            [
                dbc.ModalHeader("Transaction Successful"),
                dbc.ModalBody("Data successfully added to the database and transaction completed successfully."),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close-button", className="ml-auto", n_clicks=0
                    )
                ),
            ],
            id="success-confirmation",
            is_open=False,
        ),

    ]
)
