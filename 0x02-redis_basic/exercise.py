#!/usr/bin/env python3
"""script for using redis in py"""
from typing import Union, Callable
from functools import wraps
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """this is a decorator to keep track of the count calls"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """this is a wrapper"""
        self._redis.incr(method.__qualname__, 1)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """Cache class for redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method to store data and return a key in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, key: str) -> Union[str, None]:
        """get as str"""
        return self.get(key, str)

    def get_int(self, key: str) -> Union[int, None]:
        """get as int"""
        return self.get(key, int)

    def get(self, key: str, fn: Union[Callable] = None) -> Union[str, int, bytes, float, None]:  # noqa: E261
        """get from redius"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        else:
            return data
