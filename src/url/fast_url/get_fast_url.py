from flask import Response
from ...DB.DB_acess import *

def request_get_link(name):
    try:
        return get_link(name)
    except:
        return Response(
            'Esta url não existe',
            status = 400
        )

def get(name):
    return get_fast_url(name)

def get_link(name):
    doc = get(name)
    print(doc)
    return doc['link']

def exists(name):
    return exists_fast_url(name)