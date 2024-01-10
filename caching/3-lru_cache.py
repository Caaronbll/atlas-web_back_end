#!/usr/bin/env python3
"""task 3 - making a custon LRU cache system"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Last Recently Used cache that inherits from BaseCaching
    """
    def __init__(self):
        """Initialize the LRUCache class
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Move existing key to end to mark it as most recently used
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Remove least recently used item (first item in OrderedDict)
                lru_key, _ = self.order.popitem(last=False)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

            # Add the new item to the cache and mark it as most recently used
            self.cache_data[key] = item
            self.order[key] = None

    def get(self, key):
        """ Get an item by key to the cache
        """
        if key is not None and key in self.cache_data:
            # Move the key to the end to mark it as most recently used
            del self.order[key]
            self.order[key] = None
            return self.cache_data[key]
        return None
