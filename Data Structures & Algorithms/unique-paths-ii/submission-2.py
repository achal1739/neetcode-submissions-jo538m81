class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        def dfs(row, col):
            if row >= rows or col >= cols:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == rows - 1 and col == cols - 1:
                return 1
            if (row, col) in memo:
                return memo[(row,col)]
            
            memo[(row,col)] = dfs(row+1, col) + dfs(row, col+1)
            return memo[(row, col)]
        
        return dfs(0,0)