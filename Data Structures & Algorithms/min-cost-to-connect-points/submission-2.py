from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        min_heap = [[0,0]]

        while len(visit) < len(points):
            cost, point = heapq.heappop(min_heap)

            if point in visit:
                continue
            res += cost
            visit.add(point)

            for nei_cost, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(min_heap, [nei_cost, nei])

        return res