class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = defaultdict(int)

        for i in range(n):
            prices[i] = float("inf")
        prices[src] = 0
        
        for i in range(k+1):
            temp = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            
            prices = temp
        
        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]