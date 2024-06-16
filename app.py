from flask import Flask, request, Response
from flask_cors import CORS
import os
from src.url.fast_url.fast_url_service import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": os.getenv('ORIGIN_FRONT'), "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": ["Content-Type"]}})

@app.route('/')
def homepage():
    return 'ON'

@app.route('/fast', methods = ['POST'])
def create_fast_url():
    link = request.args.get('link')
    return request_create_fast_url(link)

@app.route('/fast', methods = ['GET'])
def redirect():
    try:
        return request_get_link(request.args.get('hash'))
    except:
        return Response(
            'Esta url não existe',
            status = 400
        )
    