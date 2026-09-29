class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sub = []
        output = []

        def dfs(open_count, close_count):
            if open_count == close_count == n:
                output.append("".join(sub))
                return
            
            if open_count < n:
                sub.append("(")
                dfs(open_count+1, close_count)
                sub.pop()
            
            if close_count < open_count:
                sub.append(")")
                dfs(open_count, close_count+1)
                sub.pop()
        
        dfs(0,0)
        return output