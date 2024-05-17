#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Define MRUCache"""

    def __init__(self):
        """Initialize MRUCache"""
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """assign item to the dict"""
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
        """return value associated with key"""
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
