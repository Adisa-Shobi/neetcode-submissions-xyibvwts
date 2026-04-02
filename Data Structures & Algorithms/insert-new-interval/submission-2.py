class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newInterval = [newInterval]
        def addNew(arr, new):
            if arr and arr[-1][1] >= new[0]:
                arr[-1][1] = max(arr[-1][1], new[1])
            else:
                arr.append(new)
        
        a, b = 0, 0
        nA, nB = len(intervals), len(newInterval)
        res = []

        while a < nA or b < nB:
            currA, currB = None, None
            if a < nA:
                currA = intervals[a]
            if b < nB:
                currB = newInterval[b]
            nxt = currA
            if not nxt or (currB and currB[0] < nxt[0]):
                nxt = currB
                b += 1
            else:
                a += 1
            addNew(res, nxt)
        return res
            


        

