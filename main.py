from flask import Flask, request, Response
from flask_cors import CORS
from src.url.fast_url.create_fast_url import *
from src.url.fast_url.get_fast_url import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": ["Content-Type"]}})

@app.route('/')
def homepage():
    return 'ON'

@app.route('/create/fast', methods = ['POST'])
def create_fast_url():
    name = request.args.get('name')
    link = request.args.get('link')
    return request_create_fast_url(name, link)

@app.route('/<name>', methods = ['GET'])
def redirect(name):
    try:
        return request_create_fast_url(name)
    except:
        return Response(
            'Esta url não existe',
            status = 400
        )
