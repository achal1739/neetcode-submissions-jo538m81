class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        output = []

        for x,y in points:
            dist = (x**2) + (y**2)
            minheap.append([dist, x, y])
        
        heapq.heapify(minheap)
        while k:
            val = heapq.heappop(minheap)
            output.append([val[1], val[2]])
            k -= 1
        
        return output
