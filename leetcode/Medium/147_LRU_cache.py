# Case 1: Use hash table + stack
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.priority = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.priority.remove(key)
        self.priority.append(key)
        return self.cache[self.priority[-1]]

    def put(self, key: int, value: int) -> None:
        # check overwrite
        if key in self.cache:
            self.cache[key] = value
            self.priority.remove(key)
            self.priority.append(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.pop(self.priority[0], None)
                self.priority.pop(0)
            self.cache[key] = value
            self.priority.append(key)


# Case 2: Use hash table + double linked list

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1);    #// return 1
obj.put(3, 3); #// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
obj.get(2);    #// returns -1 (not found)
obj.put(4, 4); #// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
obj.get(1);    #// return -1 (not found)
obj.get(3);    #// return 3
obj.get(4);    #// return 4


