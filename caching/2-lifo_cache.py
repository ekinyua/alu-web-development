#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache define a FIFO algorithm"""

    def __init__(self):
        """ Initiliaze"""
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """Add to the cache"""
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item
                

    def get(self, key):
        """Return value linked to the key"""
        valuecache = self.cache_data.get(key)
        return valuecache
