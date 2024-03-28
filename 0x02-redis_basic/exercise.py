#!/usr/bin/env python3
"""
Module to handle redis Caching
"""
from redis import Redis
from typing import Union, Callable, Optional, Awaitable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    counter function decorator
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Function to track inputs and outputs
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Function to store input and outputs
        """
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(output))
        return output

    return wrapper


def replay(method: Callable) -> None:
    """
    Function to diplay method call history

    args:
        method: function to track
    """
    name = method.__qualname__
    cache = Redis()
    calls = str(cache.get(name))
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    redis_all = list(zip(input, outputs))

    for i, o in redis_all:
        print("{}(*{}) -> {}".format(name, str(i), str(o)))


class Cache:
    """
    Class to handle redis instances

    atr:
        _redis: redis connection
    """

    def __init__(self) -> None:
        """
        Initialize function that create redis connection
          instance
        """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method to store the provide data into redis

        args:
            data: data to store

        return: the Key of object
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None, Awaitable]:
        """
        Method to retrieve data from redis

        args:
            key: key for the data
            fn: function to convert data

        return: data
        """
        data = self._redis.get(key)

        if data is None:
            return None

        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """
        Method to convert bytes to string

        args:
            key: data key

        return: str
        """
        value = self._redis.get(key)
        return str(value)


def get_int(self, key: str) -> int:
    """
    Method to retrieve an integer value from Redis.

    Args:
        key: The key to retrieve the integer value from.

    Returns:
        int: The retrieved integer value.
    """
    value = self._redis.get(key)
    if value is None:
        return 0
    return int(value.decode("utf-8"))
