from flask import Flask, render_template, Response
from random import randint
import json

app = Flask(__name__)


@app.route("/data")
def chart_data():
    data_set = []

    for x in range(0, 12):
        y = randint(1, 12)
        data_set.append(y)

    data = {'set': data_set}

    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')

    return resp


@app.route("/")
def hello():
    data = {'title': 'Chart'}

    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
