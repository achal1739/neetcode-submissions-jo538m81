import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        while lower < upper:
            k = (lower+upper)//2
            count = 0

            for i in range(len(piles)):
                count += math.ceil(piles[i]/k)
            
            if count > h:
                lower = k+1
            else:
                upper = k
            
        return lower
        

