#!/usr/bin/env python3
"""script for using redis in py"""
from typing import Union, Callable
from functools import wraps
import redis
import uuid
import requests

redis = redis.Redis()


def call_tracker(f: Callable) -> Callable:
    """this is a decorator to keep track of the history"""

    @wraps(f)
    def wrapper(*args, **kwds):
        """this is a wrapper"""
        url = args[0]
        redis.incr(f'count:{url}', 1)
        output = redis.get(url)
        if output:
            return output
        return f(*args, **kwds)
    return wrapper


@call_tracker
def get_page(url: str) -> str:
    """get page source code"""
    try:
        response = requests.get(url)
        output = response.text
        redis.set(url, output)
        redis.expire(url, 10)
        return output
    except Exception:
        pass
