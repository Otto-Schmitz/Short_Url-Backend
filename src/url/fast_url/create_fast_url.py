from flask import Response
from datetime import datetime, timedelta
from ...DB.DB_acess import *

def request_create_fast_url(name, link):
    try:
        return Response(
            create(name, link),
            status = 201
        )
    except:
        return Response(
            'Unable to create link',
            status = 400
        )

def create(name, link):
    if exists_fast_url(name):
        raise Exception('Unable to create link')

    current_time = datetime.now()
    expiration_date = current_time + timedelta(days=365 * 10)

    doc = {
        "name":name,
        "link":link,
        "active":True,
        "created":current_time,
        "expiration":expiration_date
    }

    return create_fast_url(doc)
