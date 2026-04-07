class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1, len(res)):
            curr = i
            add = curr % 2
            res[i] = res[curr // 2] + add
        return res
        