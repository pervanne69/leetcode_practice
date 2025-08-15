


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = dict()

    def get(self, key: int) -> int:
        if key in self.values:

            return self.values[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.values) == self.capacity:
            del self.values[self.last_recent_used]
        self.values[key] = [value, 0]
        if self.last_recent_used is None:
            self.last_recent_used = key



lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))