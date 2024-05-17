#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Defining BasicCache"""

    def put(self, key, item):
        """
            modify cache data

            Args:
                key: of the dict
                item: value of the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve values from cache"""
        if key is None or key not in self.cache_data:
            return None
        valuecache = self.cache_data.get(key)
        return valuecache
