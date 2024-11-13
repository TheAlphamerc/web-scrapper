from flask import Flask, request
from util import convert
from flask_cors import CORS
from flask import jsonify
from flask import make_response
# from html2image import Html2Image


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


# @app.route("/api/meta")
# def linkMetaPreview():
#     url = request.args.get('url')
#     if url is None:
#         return {'error': 'url is missing in params'}, 400
#     url = convert(url)
#     json = readMeta(url)

#     return render_template("image.html", data=json)


@app.route("/api/img")
def api_image():
    url = request.args.get('url')
    if url is None:
        return {'error': 'url is missing in params'}, 400
    url = convert(url)
    # hti = Html2Image(temp_path="./tmp")
    # list = hti.screenshot(url=url, size=(720, 454),)
    # print(list)
    return {'result': 'success'}


@app.route('/api/read_url_meta')
def read_url_meta():
    # Get urls from params
    url = request.args.get('url')
    if url is None:
        return {'error': 'url is missing in params'}, 400
    url = convert(url)

    print(url)
    result = readMeta(url)
    response = make_response(jsonify({'result': result}))
    # Add cache control headers to response. This will cache the response for 365 days
    response.headers['Cache-Control'] = 'public, max-age=31536000'
    # Add expires header to response. This will cache the response for 30 days
    response.headers['Expires'] = '31536000'
    return response


@app.route('/api/meta/nostra')
def nostraMeta():
    # Get urls from params
    url = request.args.get('url')
    if url is None:
        return {'error': 'url is missing in params'}, 400
    url = convert(url)

    print(url)
    result = readMeta(url)
    response = make_response(jsonify({'result': result}))
    # Add cache control headers to response. This will cache the response for 365 days
    response.headers['Cache-Control'] = 'public, max-age=31536000'
    # Add expires header to response. This will cache the response for 30 days
    response.headers['Expires'] = '31536000'
    return response


@app.route('/api/meta/pensil')
def pensilMeta():
    # Get urls from params
    url = request.args.get('url')
    if url is None:
        return {'error': 'url is missing in params'}, 400
    url = convert(url)

    print(url)
    result = readMeta(url)
    response = make_response(jsonify({'result': result}))
    # Add cache control headers to response. This will cache the response for 365 days
    response.headers['Cache-Control'] = 'public, max-age=31536000'
    # Add expires header to response. This will cache the response for 30 days
    response.headers['Expires'] = '31536000'
    return response


@app.route('/api/meta/humbl')
def humblMeta():
    # Get urls from params
    url = request.args.get('url')
    if url is None:
        return {'error': 'url is missing in params'}, 400
    url = convert(url)

    print(url)
    result = readMeta(url)
    response = make_response(jsonify({'result': result}))
    # Add cache control headers to response. This will cache the response for 365 days
    response.headers['Cache-Control'] = 'public, max-age=31536000'
    # Add expires header to response. This will cache the response for 30 days
    response.headers['Expires'] = '31536000'
    return response


@app.errorhandler(404)
def handle_exception(e):
    print('\nERROR:', e)
    return {'error': 'Not found'}, 404


@app.errorhandler(Exception)
def handle_exception(e):
    print('\nERROR:', e)
    return {'error': 'something went wrong'}, 500
