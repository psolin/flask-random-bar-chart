from flask import Flask, render_template, Response
from random import randint
import json

app = Flask(__name__)

@app.route("/data")
def chart_data():
    # Generate a dataset with 12 random integers
    data_set = [randint(1, 12) for _ in range(12)]

    # Prepare the response
    data = {'set': data_set}
    response = Response(json.dumps(data), status=200, mimetype='application/json')

    return response

@app.route("/")
def hello():
    # Render the index template with a title
    data = {'title': 'Chart'}
    return render_template('index.html', data=data)

if __name__ == "__main__":
    # Run the app in debug mode
    app.run(debug=True)
