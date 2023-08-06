from flask import Flask, request
from util import convert
from flask_cors import CORS
from flask import jsonify
from flask import make_response


from read_meta_data import readMeta

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def home():
    return "Hello, World!"


@app.route("/api")
def api():
    response = make_response(jsonify({"data": "some data"}))
    response.headers['Cache-Control'] = 'public, max-age=300'
    return response


@app.route('/api/read_web_meta_data')
def read_web_meta_data():
    # Get urls from params
    url = request.args.get('url')
    if url is None:
        return {'error': 'url is missing in params'}, 400
    url = convert(url)

    print(url)
    result = readMeta(url)
    response = make_response(jsonify({'result': result}))
    # Add cache control headers to response. This will cache the response for 30 days
    response.headers['Cache-Control'] = 'public, max-age=2592000'
    # Add expires header to response. This will cache the response for 30 days
    response.headers['Expires'] = '2592000'
    return response


@app.errorhandler(404)
def handle_exception(e):
    print('\nERROR:', e)
    return {'error': 'Not found'}, 404


@app.errorhandler(Exception)
def handle_exception(e):
    print('\nERROR:', e)
    return {'error': 'something went wrong'}, 500
