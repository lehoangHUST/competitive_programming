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
class Node:
    def __init__(self, data, prev=None, next=None):
        self.item = data
        self.prev = prev
        self.next = next
        
class DoubleLinkedList:
    def __init__(self):
        self.list_node = None
        self.length = 0
    
    def put(self, data):
        if self.list_node is None:
            self.list_node = Node(data, None, None)
            self.length += 1    
            return
        n = self.list_node
        while n.next is not None:
            n = n.next
        new_node = Node(data, n, None)
        n.next = new_node
        self.length += 1
        return
    
    def __len__(self):
        return self.length

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# obj.get(1);    #// return 1
# obj.put(3, 3); #// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# obj.get(2);    #// returns -1 (not found)
# obj.put(4, 4); #// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# obj.get(1);    #// return -1 (not found)
# obj.get(3);    #// return 3
# obj.get(4);    #// return 4

doubleLL = DoubleLinkedList()
doubleLL.put(3)
doubleLL.put(5)
print(len(doubleLL))