from datetime import datetime, timedelta
from ..fast_url.fast_url_service import count_total_clicks_fast_url
from ...DB.DB_click_acess import *

def _create_clicks():
    create_clicks({
        'total_clicks': count_total_clicks_fast_url(),
        'last_update': datetime.now()
    })

def add_clicks():
    if get_clicks() is None :
        _create_clicks()
    else:
        update_clicks(datetime.now())