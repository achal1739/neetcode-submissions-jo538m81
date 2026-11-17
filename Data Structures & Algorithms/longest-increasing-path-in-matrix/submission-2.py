class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {}

        def dfs(r, c, prev):
            if r not in range(rows) or c not in range(cols) or matrix[r][c] <= prev:
                return 0
            if (r,c) in dp:
                return dp[(r, c)]
            
            result = 1
            result = max(result, 1 + dfs(r + 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r, c + 1, matrix[r][c]))
            result = max(result, 1 + dfs(r - 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r,c)] = result
            return result
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        
        return max(dp.values())