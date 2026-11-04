from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [(0, k)]
        t = 0
        visit = set()

        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            visit.add(node)
            t = max(t, weight)

            for nei, wei in edges[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (weight + wei, nei))
        
        if len(visit) == n:
            return t
        else:
            return -1