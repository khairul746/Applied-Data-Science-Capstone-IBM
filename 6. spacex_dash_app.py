import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import seaborn as sns

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv",index_col=0)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}
                                        ),
                                html.Div(children=[dcc.Dropdown(id='site-dropdown',options=[
                                                            {'label':'All Sites','value':'ALL'},
                                                            {'label':'CCAFS LC-40','value':'CCAFS LC-40'},
                                                            {'label':'VAFB SLC-40','value':'VAFB SLC-40'},
                                                            {'label':'KSC LC-39A','value':'KSC LC-39A'},
                                                            {'label':'CCAFS SLC-40','value':'CCAFS SLC-40'}
                                                            ],
                                                            value='ALL',
                                                            placeholder='place holder here',
                                                            searchable=True
                                                             ),
                                                    html.Div(dcc.Graph(id='success-pie-chart'))
                                                    ]
                                        ),
                                html.Div(children=[html.P("Payload range (Kg):"),
                                                   (dcc.RangeSlider(id='payload-slider',
                                                                    min=0, max=10_000, step=1000,
                                                                    marks={0:'0',
                                                                            1000:'1000',2000:'2000',3000:'3000',4000:'4000',
                                                                            5000:'5000',6000:'6000',7000:'7000',8000:'8000',
                                                                            9000:'9000',10000:'10000'},
                                                                    value=[min_payload, max_payload]
                                                                    )
                                                    ),
                                                   html.Div(dcc.Graph(id='success-payload-scatter-chart'))
                                                   ]
                                                   
                                        )
                                ]
                    )

# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df[['Launch Site','class']]
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', names='Launch Site', title='Total Success Launched by Site')
        return fig
    else:
        selected_launch = filtered_df[filtered_df['Launch Site']==entered_site]
        selected_launch = selected_launch['class'].value_counts().reset_index()
        fig = px.pie(selected_launch,
                     values='class',names='index',title=f'Total Success Launched by Site {entered_site}')
        return fig

# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site,entered_payload):
    filtered_df = spacex_df[['Launch Site','Booster Version Category','Payload Mass (kg)','class']]
    filtered_df = filtered_df[(filtered_df['Payload Mass (kg)']>=entered_payload[0]) \
                              & (filtered_df['Payload Mass (kg)']<=entered_payload[1])]
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df,x='Payload Mass (kg)',y='class',
                                   color='Booster Version Category',
                                   title='Correlation between Payload and Success for all Sites')
        return fig
    else :
        filtered_df = filtered_df[filtered_df['Launch Site']==entered_site]
        fig = px.scatter(filtered_df,x='Payload Mass (kg)',y='class',
                                   color='Booster Version Category',
                                   title=f'Correlation between Payload and Success for Site {entered_site}')
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
