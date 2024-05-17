#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ 
        Defines a FIFO algorithm to use cache
    """

    def __init__(self):
        """ Initiliaze"""
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """Assigning item value to the dict"""
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print("DISCARD: {}".format(delete))

    def get(self, key):
        """Output the value linked to the key"""
        return self.cache_data.get(key)
