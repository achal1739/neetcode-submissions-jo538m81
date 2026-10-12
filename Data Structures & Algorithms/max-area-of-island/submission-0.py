from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        max_land = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(row,col):
            seen.add((row,col))
            area = 0
            q = deque([(row,col)])

            while q:
                r,c = q.popleft()
                area += 1

                for dr,dc in directions:
                    if (r+dr) in range(rows) and (c+dc) in range(cols) and (r+dr, c+dc) not in seen and grid[r+dr][c+dc] == 1:
                        q.append((r+dr, c+dc))
                        seen.add((r+dr, c+dc))
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    max_land = max(max_land, bfs(r,c))


        return max_land