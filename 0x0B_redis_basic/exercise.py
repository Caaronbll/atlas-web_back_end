#!/usr/bin/env python3
""" Redis basic """

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator for counting function calls """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper call method """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator for storing function call history """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper call method """
        input = str(args)
        self._redis.rpush(f"{method.__qualname__}:inputs", input)
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", output)
        return output

    return wrapper


def replay(method: Callable) -> None:
    """ Displays history of calls """

    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")

    print("{} was called {} times:".format(key, count))

    inputList = redis.lrange(inputs, 0, -1)
    outputList = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(inputList, outputList))

    for a, b in redis_zipped:
        attr, data = a.decode("utf-8"), b.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))


class Cache():
    """ Cache class """

    def __init__(self):
        """ Initialize the Cache """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in the Cache """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes, int, float]:
        """ Get data from the Cache """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """ Converts data to string """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts data to int """
        return int.from_bytes(data)
