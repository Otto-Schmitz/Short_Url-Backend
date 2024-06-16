import random
from ...DB.DB_fast_acess import *

def _create_random_hash():
    size = random.randint(3, 6)
    allowed_numbers = list(range(65, 91)) + list(range(97, 123))
    hash_chars = random.choices(allowed_numbers, k=size)

    return ''.join(chr(num) for num in hash_chars)

def create_unique_hash():
    hash = _create_random_hash()

    return create_unique_hash() if exists_url_by_hash(hash) else hash