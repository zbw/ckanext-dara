from functools import wraps
from itertools import izip_longest


def memoize(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


# build blocks of size from seq
def grouper(seq, size):
    bargs = [iter(seq)] * size
    return izip_longest(*bargs)


# build dictionary from seq with ids as keys
def dicter(seq, ids):
    return map(lambda t: dict(zip(ids, t)), seq)


# put _grouper and _dicter together; build dictionary from flat lists
# used for flat lists with multiple values in webforms, e.g authors
def list_dicter(seq, ids):
    return dicter(grouper(seq, len(ids)), ids)
