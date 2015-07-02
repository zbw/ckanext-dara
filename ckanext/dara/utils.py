from functools import wraps
from itertools import izip_longest
from ckanext.dara.schema import author_fields


def memoize(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def _grouper(seq, size):
    bargs = [iter(seq)] * size
    return izip_longest(*bargs)


def _dicter(seq, ids):
    return map(lambda t: dict(zip(ids, t)), seq)


def list_dicter(seq, fields, ids):
    return _dicter(_grouper(seq, len(fields)), ids)



