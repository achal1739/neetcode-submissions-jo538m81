class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.nxt = self.right
        self.right.prev = self.left
        
    def insert(self, key, val):
        cur = Node(key, val)
        self.cache[key] = cur
        prev = self.right.prev
        cur.nxt = self.right
        cur.prev = prev
        prev.nxt = cur
        self.right.prev = cur

    def remove(self, key):
        cur = self.cache[key]
        prev = cur.prev
        nxt = cur.nxt
        nxt.prev = prev
        prev.nxt = nxt
        del self.cache[key]


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self.remove(key)
        self.insert(key, val)
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.insert(key, value)
        
        while len(self.cache) > self.capacity:
            self.remove(self.left.nxt.key)

        

        
