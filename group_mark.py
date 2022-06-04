import pandas as pd
import numpy as np
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import pyperclip

# Create Dash application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,
                suppress_callback_exceptions=False,
                external_stylesheets=external_stylesheets)

comments = pd.read_csv("S1_2022/QBUS6840_2022S1_Comments.csv", delimiter="\t")
test_data = pd.read_csv("S1_2022/CPI_test.csv")

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(comments[comments.Category == "Task 1"].Comment.values, id='task1'),
        dcc.Textarea(value="", id='comments1', style={'height': 60}),
    ]),
    html.Div([
        dcc.Dropdown(comments[comments.Category == "Task 2"].Comment.values, id='task2'),
        dcc.Textarea(value="", id='comments2', style={'height': 60}),
    ]),
    html.Div([
        dcc.Dropdown(comments[comments.Category == "Task 3"].Comment.values, id='task3'),
        dcc.Textarea(value="", id='comments3', style={'height': 60}),
    ]),
    html.Div([
        dcc.Dropdown(comments[comments.Category == "Task 4"].Comment.values, id='task4'),
        dcc.Textarea(value="", id='comments4', style={'height': 60}),
    ]),
    html.Div([
        dcc.Textarea(value="", id='comments5', style={'height': 60}),
    ]),
    html.Button("Compute", id="button"),
    dcc.Textarea(value="", id='final'),
])


@app.callback(
    Output('comments1', 'value'),
    Input('task1', 'value'),
    State('comments1', 'value')
)
def update1(choice, previous):
    return (previous + "\n" + choice).strip()


@app.callback(
    Output('comments2', 'value'),
    Input('task2', 'value'),
    State('comments2', 'value')
)
def update2(choice, previous):
    return (previous + "\n" + choice).strip()


@app.callback(
    Output('comments3', 'value'),
    Input('task3', 'value'),
    State('comments3', 'value')
)
def update3(choice, previous):
    return (previous + "\n" + choice).strip()


@app.callback(
    Output('comments4', 'value'),
    Input('task4', 'value'),
    State('comments4', 'value')
)
def update4(choice, previous):
    return (previous + "\n" + choice).strip()


@app.callback(
    Output('comments5', 'value'),
    Input('task5', 'value'),
    State('comments5', 'value')
)
def update5(choice, previous):
    return (previous + "\n" + choice).strip()


def extract_score(txt, max_score):
    errors = [float(item.split(" ")[0]) for item in txt.splitlines()]
    minus_score = sum(errors)
    return float(max_score) + minus_score


def compute_mse(txt):
    data = []
    for line in txt.splitlines():
        try:
            val = float(line.split(",")[-1])
            data.append(val)
        except:
            print("Do nothing!")

    data = np.array(data)
    return np.mean(np.power(data - test_data.CPI, 2))


@app.callback(
    Output("final", "value"),
    Input("button", "n_clicks"),
    [
        State("comments1", "value"),
        State("comments2", "value"),
        State("comments3", "value"),
        State("comments4", "value"),
        State("comments5", "value"),
    ]
)
def get_review(clicks, comments1, comments2, comments3, comments4, comments5):
    task1_mark = extract_score(comments1, 2)
    task2_mark = extract_score(comments2, 7)
    task3_mark = extract_score(comments3, 1)
    task4_mark = extract_score(comments4, 5)
    mse = compute_mse(comments5)

    all_comments = str(task1_mark) + "\t" + comments1 + "\t" + \
                   str(task2_mark) + "\t" + comments2 + "\t" + \
                   str(task3_mark) + "\t" + comments3 + "\t" + \
                   comments4 + "\t" + str(task4_mark) + "\t" + \
                   str(mse)
    pyperclip.copy(all_comments)
    return all_comments


app.run_server(debug=False,  # needs to be false in Jupyter
               host='0.0.0.0',
               port=9900,
               # threaded=True,
               # processes=12,
               )
