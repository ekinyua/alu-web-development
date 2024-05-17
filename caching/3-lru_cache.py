#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache algorithm"""

    def __init__(self):
        """ Initiliaze"""
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """Assign item to the dict"""
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """Return value linked to the specific key"""
        valuecache = self.cache_data.get(key)

        if valuecache:
            self.queue.remove(key)
            self.queue.append(key)
        return valuecache
