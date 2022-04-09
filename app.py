from flask import Flask, render_template, request, url_for
import requests
import sys
from subprocess import run, PIPE
from pathlib import Path
from .forms import MyForm

# SECRET_KEY = '8e047de3585dee0d62505148bea92ac841390fbb63e47075'

# The root directory
BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)


@app.route("/")
def hello_world():
	# data = requests.get("http://google.com/")
	# print(data.text)
	# data = data.text
	return render_template(
		'index.html', 
		# data=data
		)


@app.route("/external", methods=['POST', 'GET'])
def external():
	name = request.form.get('fname')
	email = request.form.get('email')
	note = request.form.get('note')
	r_out = 'Output displays here...'
	if name is not None:
		out = run([sys.executable, BASE_DIR/'scripts/test.py', name, email, note], shell=False, stdout=PIPE)
		r_out = out.stdout
	# print(out)
	# form = MyForm()
	return render_template('out.html', data=r_out)


if __name__ == "__main__":
	app.run(host='127.0.0.1', debug=True)
