#!/usr/bin/env python3
"""task 2 - making a custon LIFO cache system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last in first out cache that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the LIFOCache class
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using LIFO algorithm
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, remove the last item (LIFO)
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
