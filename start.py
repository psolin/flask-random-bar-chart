from flask import Flask, render_template
from random import randint
import time

app = Flask(__name__)

def wave(max_line):

	# The min/max size of the lines
	size = randint(3,max_line)

	line = []

	# Line beginning
	for i in range(0,size):
		line.append(('=' * i) + ('=' * i))

	# Line Middle
	line.append(('=' * (size+size)))

	# Wave ending
	for i in range(0,size):
		size -= 1
		line.append(('=' * size) + ('=' * size))

	line.append('=')

	return line

@app.route("/")
def hello(data=None):

	data = {}

	data['wave'] = []

	for index in range(0,150):
		for item in wave(randint(5,20)):
			data['wave'].append(item)

	data['title'] = 'This Is The Wave'

	return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)