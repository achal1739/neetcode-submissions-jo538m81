class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        min_heap = [[grid[0][0], 0, 0]]
        visit.add((0,0))

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return t
            
            for dr, dc in directions:
                if (r+dr) not in range(rows) or (c+dc) not in range(cols) or (r+dr, c+dc) in visit:
                    continue
                visit.add((r+dr, c+dc))
                heapq.heappush(min_heap, (max(t, grid[r+dr][c+dc]), r+dr, c+dc))
                