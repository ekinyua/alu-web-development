#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ 
        Defines a FIFO algorithm

      To use:
      >>> my_cache = BasicCache()
      >>> my_cache.print_cache()
      Current cache:

      >>> my_cache.put("A", "Hello")
      >>> my_cache.print_cache()
      A: Hello

      >>> print(my_cache.get("A"))
      Hello

      Ex:
      >>> print(self.cache_data)
      {A: "Hello", B: "World", C: "Holberton", D: "School"}
      >>> my_cache.put("C", "Street")
      >>> print(self.cache_data)
      {A: "Hello", B: "World", C: "Street", D: "School"}

      >>> my_cache.put("F", "COD")
      DISCARD: A
      >>> print(self.cache_data)
      {F: "COD", B: "World", C: "Holberton", D: "School"}
    """

    def __init__(self):
        """ Initiliaze
        """
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
