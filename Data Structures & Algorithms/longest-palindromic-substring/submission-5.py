class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        n = len(s)

        for i in range(n):
            # odd
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                length = (r - l + 1)
                if length > resLen:
                    res = s[l:r + 1]
                    resLen = length
                l -= 1
                r += 1
                
            # even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                length = (r - l + 1)
                if length > resLen:
                    res = s[l:r + 1]
                    resLen = length
                l -= 1
                r += 1
        return res
