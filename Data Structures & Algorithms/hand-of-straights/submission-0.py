import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            
            for i in range(start, start + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if min_heap[0] != i:
                        return False
                    else:
                        heapq.heappop(min_heap)
        
        return True

