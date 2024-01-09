#!/usr/bin/env python3
"""task 1 - making a custon FIFO cache system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """First in first out cache that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the FIFOCache class
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, remove the first item (FIFO)
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
