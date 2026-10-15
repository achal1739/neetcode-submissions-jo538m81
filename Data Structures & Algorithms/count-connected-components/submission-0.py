class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        self.output = 0
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()

        def dfs(i):
            if i in visit:
                return
            
            visit.add(i)
            
            for j in adj[i]:
                dfs(j)
        
        count = 0

        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count