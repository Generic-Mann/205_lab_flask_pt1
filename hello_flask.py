from flask import Flask
from flask import render_template
from flask import url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
  return 'Hello World!'


@app.route('/michael')
def evil():
  return render_template('michael.html')


