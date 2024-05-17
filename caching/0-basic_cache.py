#!/usr/bin/python3
""" 
    BaseCache module 

"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ 
        BasicCache defines a intro to use cache

      To use:
      >>> my_cache = BasicCache()
      >>> my_cache.print_cache()
      Current cache:

    """
    def put(self, key, item):
        """
            modify cache data

            Args:
                key: of the dict
                item: value of the key
        """
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            modify cache data

            Args:
                key: of the dict

            Return:
                value
        """

        valuecache = self.cache_data.get(key)
        return valuecache
