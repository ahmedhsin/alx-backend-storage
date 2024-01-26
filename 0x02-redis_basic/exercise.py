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


def call_history(method: Callable) -> Callable:
    """this is a decorator to keep track of the history"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """this is a wrapper"""
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(method.__qualname__ + ':outputs', str(output))
        return output
    return wrapper


def replay(f: Callable) -> None:
    """fuc to display info """
    key = f.__qualname__
    self = f.__self__
    call_times = self.get_int(key)
    tim = 'times'
    if call_times == 1:
        tim = 'time'
    if call_times:
        print(f'{key} was called {call_times} {tim}:')
    inputs = self._redis.lrange("{}:inputs".format(key), 0, -1)
    outputs = self._redis.lrange("{}:outputs".format(key), 0, -1)
    for k, v in zip(inputs, outputs):
        k = k.decode('utf-8')
        v = v.decode('utf-8')
        print(f'{key}(*{k}) -> {v}')


class Cache:
    """Cache class for redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
