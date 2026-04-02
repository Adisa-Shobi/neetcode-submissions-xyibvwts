class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        res = [intervals[0]]
        skip = 0
        prev = res[-1]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] > curr[0]:
                if curr[1] > prev[1]:
                    curr = prev
                prev = curr
                skip += 1
                continue
            prev = curr
        return skip
            
