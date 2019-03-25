"""
This module will allow caching of data and expiry based on oldest cached value
once the maximum allowed cached items is reached.

class will contain a dictionary of values

each value will be a dictionary with a

    value cached
    time when cached

setting a new value will
    set an item in the current dictionary
    set the new item's accessed time (via queue)

getting an item from the dictionary will
    return the item if it exists and is not stale
    reset the items accessed time

"""
import time

class Lru():
    def __init__(self, max_size=5, stale_delay=10):
        self.values = {}
        self.keys = []
        self.max_size = max_size
        self.STALE_DELAY = stale_delay

    def __contains__(self, key):
        return key in self.values

    def get_value(self, key):
        """Return value if it exists and is not stale
        """
        value = self.values.get(key, None)
        if value:
            if value['time'] + self.STALE_DELAY > time.time():
                self.delete_key(key)
                return None
            self.keys.insert(0, self.keys.pop(self.keys.index(key)))
        return value['value']

    def set_value(self, key, value):
        """Add value to key"""
        self.values[key] = {}
        self.values[key]['value'] = value
        self.values[key]['time'] = time.time()
        if not key in self.keys:
            self.keys.insert(0, key)
        if len(self.keys) > self.max_size:
            del self.values[self.keys[-1]]
            del self.keys[-1]

    def delete_key(self, key):
        """Delete key from self.values"""
        if key in self.values:
            del self.values[key]
            del self.keys[self.keys.index(key)]

    def __str__(self):
        self.clear_stale()
        return str (self.values)

    def get_values(self):
        """Get non stale values form self.values"""
        self.clear_stale()
        return [ self.values[e]['value'] for e in self.values ] 

    def wipe(self):
        """Deletes all values in self.values"""
        self.values = {}
        self.keys = []

    def clear_stale(self):
        """This will delete stale values base on creation time"""
        for e in self.keys[::-1]:
            if self.values.get(e)['time'] + self.STALE_DELAY < time.time():
                self.delete_key(e)
            else:
                # items newer than a non stale item can't be stale
                break
                
