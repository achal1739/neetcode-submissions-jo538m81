class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        sub = []

        def is_pal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def dfs(i):
            if i == len(s):
                output.append(sub.copy())
                return
            
            for j in range(i, len(s)):
                if is_pal(i,j):
                    sub.append(s[i:j+1])
                    dfs(j+1)
                    sub.pop()

        dfs(0)
        return output