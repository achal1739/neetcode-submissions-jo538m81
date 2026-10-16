class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        idx = 0

        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            output.append(intervals[idx])
            idx += 1
        
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval = [min(intervals[idx][0], newInterval[0]), max(intervals[idx][1], newInterval[1])]
            idx += 1
        
        output.append(newInterval)
        output.extend(intervals[idx:])
        return output