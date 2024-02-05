#!/usr/bin/env python3
""" Redis basic """

import redis
import uuid
from typing import Union, Callable


class Cache():
    """ Cache class """

    def __init__(self):
        """ Initialize the Cache """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
