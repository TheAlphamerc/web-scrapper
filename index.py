from flask import Flask, request
from util import convert


from read_meta_data import readMeta

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/api/read_web_meta_data')
def read_web_meta_data():
    # Get urls from params
    url = request.args.get('url')
    if url is None:
        return {'error': 'url is missing in params'}, 400
    url = convert(url)

    print(url)
    result = readMeta(url)
    return {'result': result}


@app.errorhandler(404)
def handle_exception(e):
    print('\nERROR:', e)
    return {'error': 'Not found'}, 404


@app.errorhandler(Exception)
def handle_exception(e):
    print('\nERROR:', e)
    return {'error': 'something went wrong'}, 500
