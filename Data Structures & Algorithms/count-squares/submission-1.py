from collections import defaultdict
class CountSquares:
    def __init__(self):
        self.points_cnt = defaultdict(int)
        self.pts = []
        

    def add(self, point: List[int]) -> None:
        self.points_cnt[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x,y in self.pts:
            if (abs(px-x) != abs(py-y)) or px==x or py==y:
                continue
            
            res += self.points_cnt[(x, py)] * self.points_cnt[(px, y)]
        
        return res
