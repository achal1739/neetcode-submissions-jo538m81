class Node:
    def __init__(self, val, prev = None, nxt = None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.nxt = self.right
        self.right.prev = self.left
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = Node(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.nxt = node
    
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            nxt = node.nxt
            prev = node.prev
            prev.nxt = nxt
            nxt.prev = prev
            self.map.pop(val, None)
    
    def popLeft(self):
        res = self.left.nxt.val
        self.pop(self.left.nxt.val)
        return res
    
    def update(self, val):
        self.pop(val)
        self.pushRight(val)


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.valueMap = {}
        self.lfuCnt = 0
        self.countMap = collections.defaultdict(int)
        self.listMap = collections.defaultdict(LinkedList)
        
    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valueMap:
            return -1
        self.counter(key)
        return self.valueMap[key]
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key not in self.valueMap and len(self.valueMap) == self.cap:
            res = self.listMap[self.lfuCnt].popLeft()
            self.valueMap.pop(res)
            self.countMap.pop(res)

        is_new = key not in self.valueMap
        self.valueMap[key] = value
        self.counter(key)
        if is_new:
            self.lfuCnt = 1
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)