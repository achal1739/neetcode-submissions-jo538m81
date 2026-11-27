from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs((px-x)) != abs((py-y))) or x==px or y==py:
                continue
            res += self.pts_count[(px, y)] * self.pts_count[(x, py)]
        
        return res
        
