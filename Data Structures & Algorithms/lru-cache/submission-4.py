class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)

        self.right.prev = self.left
        self.left.nxt = self.right

    def insert(self, key, val):
        node = Node(key, val)
        self.cache[key] = node
        prev = self.right.prev
        prev.nxt = node
        self.right.prev = node
        node.prev = prev
        node.nxt = self.right

    
    def delete(self, key):
        node = self.cache[key]
        nxt = node.nxt
        prev = node.prev
        nxt.prev = prev
        prev.nxt = nxt
        del self.cache[key]

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.delete(key)
            self.insert(key, val)
            return val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(key)
        
        self.insert(key, value)
        
        while len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.delete(lru.key)