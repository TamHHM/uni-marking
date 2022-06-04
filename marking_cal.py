import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# Create Dash application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,
                suppress_callback_exceptions=False,
                external_stylesheets=external_stylesheets)


app.layout = html.Div([
	html.Div([
		dcc.Textarea(value="() 0", id='comments1', style={'width':300,'height': 60}),
		dcc.Textarea(value="7", id='max_score1', style={'height': 60}),
		dcc.Textarea(value="0", id='final_score1', style={'height': 60})
	]),
		html.Div([
		dcc.Textarea(value="() 0", id='comments2', style={'width':300,'height': 60}),
		dcc.Textarea(value="10", id='max_score2', style={'height': 60}),
		dcc.Textarea(value="0", id='final_score2', style={'height': 60})
	]),
		html.Div([
		dcc.Textarea(value="() 0", id='comments3', style={'width':300,'height': 60}),
		dcc.Textarea(value="8", id='max_score3', style={'height': 60}),
		dcc.Textarea(value="0", id='final_score3', style={'height': 60})
	])
	])

@app.callback(
    Output('final_score1', 'value'),
    Input('comments1', 'value'),
    Input('max_score1', 'value')
)
def update1(comments, max_score):
	errors = [float(item.split(" ")[1]) for item in comments.splitlines()	]
	minus_score = sum(errors)
	return float(max_score) + minus_score

@app.callback(
    Output('final_score2', 'value'),
    Input('comments2', 'value'),
    Input('max_score2', 'value')
)
def update2(comments, max_score):
	errors = [float(item.split(" ")[1]) for item in comments.splitlines()	]
	minus_score = sum(errors)
	return float(max_score) + minus_score

@app.callback(
    Output('final_score3', 'value'),
    Input('comments3', 'value'),
    Input('max_score3', 'value')
)
def update3(comments, max_score):
	errors = [float(item.split(" ")[1]) for item in comments.splitlines()	]
	minus_score = sum(errors)
	return float(max_score) + minus_score


app.run_server(debug=False,  # needs to be false in Jupyter
               host='0.0.0.0',
               port=9900,
               # threaded=True,
               # processes=12,
               )