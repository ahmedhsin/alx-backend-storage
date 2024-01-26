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
        output = redis.get(url)
        if output:
            redis.incr(f'count:{url}', 1)
            return output.decode('utf-8')
        return f(*args, **kwds).decode('utf-8')
    return wrapper


@call_tracker
def get_page(url: str) -> str:
    """get page source code"""
    try:
        response = requests.get(url)
        output = response.text
        redis.setex(url, 10, output)
        return output
    except Exception:
        return ""
