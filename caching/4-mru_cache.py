#!/usr/bin/env python3
"""task 4 - making a custon MRU cache system"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Most Recently Used cache that inherits from BaseCaching
    """
    def __init__(self):
        """Initialize the MRUCache class
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Move existing key to end to mark it as most recently used
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Remove most recently used item (last item in OrderedDict)
                mru_key, _ = self.order.popitem(last=True)
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

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
