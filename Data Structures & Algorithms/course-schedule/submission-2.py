from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        seen = set()

        for a,b in prerequisites:
            preMap[a].append(b)

        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            
            
            seen.add(crs)

            for pres in preMap[crs]:
                if not dfs(pres):
                    return False
            
            seen.remove(crs)
            preMap[crs] = []
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True