#!/usr/bin/env python3
"""A python module"""

from base_caching import BaseCaching
# base_caching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Inherits from base caching"""
    def __init__(self):
        """Instance of the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item, _ = self.cache_data.popitem(False)
            print("DISCARD!", first_item)

    def get(self, key):
        """geth method"""
        return self.cache_data.get(key, None)
