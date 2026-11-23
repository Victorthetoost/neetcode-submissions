class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, m = 0, 0, 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        sub = s[0]
        r += 1
        while r < len(s):
            if s[r] in sub:
                while s[r] in sub:
                    l += 1
                    sub = s[l:r]
            else:
                r += 1
                sub = s[l:r]
            if r - l > m:
                    m = r - l
        return m
