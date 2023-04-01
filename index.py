from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/api')
def api():
    with open('data.json', 'r') as f:
        data = f.read()
    return data
