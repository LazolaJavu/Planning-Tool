from dash import Dash
# import dash_html_components as html
# import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash import html
from dash import dcc
import pandas as pd


# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1("Data Entry Form"),
#     html.Div([
#         html.Label("Name:"),
#         dcc.Input(id="name-input", type="text"),
#     ], style={"margin-bottom": "10px"}),
#     html.Div([
#         html.Label("Age:"),
#         dcc.Input(id="age-input", type="number"),
#     ], style={"margin-bottom": "10px"}),
#     html.Div([
#         html.Label("Email:"),
#         dcc.Input(id="email-input", type="email"),
#     ], style={"margin-bottom": "10px"}),
#     html.Button("Submit", id="submit-button", n_clicks=0),
#     html.Div(id="output")
# ])

# @app.callback(
#     Output("output", "children"),
#     [Input("submit-button", "n_clicks")],
#     [
#         Input("name-input", "value"),
#         Input("age-input", "value"),
#         Input("email-input", "value")
#     ]
# )
# def submit_data(n_clicks, name, age, email):
#     if n_clicks > 0:
#         # Create a dictionary with the submitted data
#         data = {
#             "Name": [name],
#             "Age": [age],
#             "Email": [email]
#         }
#         # Convert the dictionary to a DataFrame
#         df = pd.DataFrame(data)
#         # Save the DataFrame to an Excel file
#         df.to_excel("submitted_data.xlsx", index=False)
        
#         return html.Div([
#             html.H3("Submitted Data:"),
#             html.P(f"Name: {name}"),
#             html.P(f"Age: {age}"),
#             html.P(f"Email: {email}"),
#             html.P("Data saved to submitted_data.xlsx")
#         ])
# if __name__ == "__main__":
#     app.run_server(debug=True)

data = pd.read_excel("C:/Users/LazolaJavu/OneDrive - SmartStart/Documents/SmartStart/Ops Department/Mapaseka's Request'/Planning Tool - Coaches/Models/Planning_Model v.02.xlsx")

app = Dash(__name__)

app.layout = html.Div(
    children = [
    html.H1(children = "Data SmartStart"),
    html])