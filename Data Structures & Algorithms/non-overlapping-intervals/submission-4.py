class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        skip = 0
        prev = intervals[0]
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
            
