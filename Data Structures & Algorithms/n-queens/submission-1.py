class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        posi_diag = set()
        neg_diag = set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                output.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posi_diag or (r-c) in neg_diag:
                    continue
                
                cols.add(c)
                posi_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = "Q"
                backtrack(r + 1)

                cols.remove(c)
                posi_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return output


                