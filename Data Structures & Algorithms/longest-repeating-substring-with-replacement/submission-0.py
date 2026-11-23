class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l,r,ret = 0,0,0
        while r < len(s):
            if s[r] in counts:
                counts[s[r]] = counts.get(s[r]) +1
            else:
                counts[s[r]] = 1
            while (sum(counts.values()) - max(counts.values())) > k:
                counts[s[l]] = counts.get(s[l]) - 1
                l +=1
            if r-l +1 > ret:
                ret = r-l +1
            r+=1
        return ret
