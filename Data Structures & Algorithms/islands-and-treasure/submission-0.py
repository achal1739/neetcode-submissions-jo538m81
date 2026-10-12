from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        q = deque()
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                if (r+dr) in range(rows) and (c+dc) in range(cols) and grid[r+dr][c+dc]==INF:
                    grid[r+dr][c+dc] = grid[r][c] + 1
                    q.append((r+dr, c+dc))

                
                    
                

        

