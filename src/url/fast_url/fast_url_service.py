from flask import Response
from datetime import datetime, timedelta
from ..hash.create_hash import create_unique_hash
from ...DB.DB_fast_acess import *
from ..clicks.clicks_service import add_clicks

def _create_fast_url(link):
    return create_fast_url({
        "hash": create_unique_hash(),
        "link": link,
        "active": True,
        "created": datetime.now(),
        "expiration": datetime.now() + timedelta(days=365 * 10),
        "clicks": 0,
    })

def request_create_fast_url(link):
    try:
        return verify_link(link)
    except:
        return Response(
            response = 'Unable to create link',
            status = 400
        )
    
def verify_link(link):
    return get_fast_url_by_link(link)['hash'] if exists_url_by_link(link) else _create_fast_url(link)

def _get_link(hash):
    return get_fast_url_by_hash(hash)['link']

def exists(hash):
    return exists_url_by_hash(hash)

def request_get_link(hash):
    try:
        link = _get_link(hash)
        add_clicks()
        return link
    except:
        return Response(
            'Esta url não existe',
            status = 400
        )
    
def get_total_clicks_fast_url():
    return count_total_clicks_fast_url()