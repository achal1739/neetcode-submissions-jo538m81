import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) >= 2:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -(x-y))
        
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0



        
    
        
        