#!/usr/bin/env python3
"""script for using redis in py"""
from typing import Union, Callable
import redis
import uuid


class Cache:
    """Cache class for redis"""
    def __init__(self):
        self._redis = redis.Redis()

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
