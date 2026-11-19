class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ret = []
        rets = []
        for l in s:
            if l == '#':
                if ret:
                    ret.pop()
            else:
                ret.append(l)
        for l in t:
            if l == '#':
                if rets:
                    rets.pop()
            else:
                rets.append(l)
        strs = "".join(ret)
        t  = "".join(rets)
        if strs == t:
            return True
        else:
            return False