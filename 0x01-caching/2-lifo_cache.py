#!/usr/bingpython3
"""A python module"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Inherits from base caching"""
    def __init__(self):
        """Instance of the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_item, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_item)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """geth method"""
        return self.cache_data.get(key, None)
