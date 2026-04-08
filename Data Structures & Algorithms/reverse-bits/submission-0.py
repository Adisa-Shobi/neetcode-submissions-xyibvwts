class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            temp = 1 & n
            res = (res << 1) | temp
            n = n >> 1
        return res
