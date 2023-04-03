from flask import Flask, request
from rfc3986 import urlparse
from read_meta_data import readMeta
import urllib

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/api')
def api():
    with open('data.json', 'r') as f:
        data = f.read()
    return data


@app.route('/read_web_meta_data')
def read_web_meta_data():
    # Get urls from params
    url = request.args.get('url')
    if url is None:
        return {'error': 'url is required'}
    url = convert(url)

    print(url)
    result = readMeta(url)
    return {'result': result}


def convert(url):
    if url.startswith('http://www.'):
        return 'http://' + url[len('http://www.'):]
    if url.startswith('www.'):
        return 'http://' + url[len('www.'):]
    if not url.startswith('http://'):
        return 'http://' + url
    return url
