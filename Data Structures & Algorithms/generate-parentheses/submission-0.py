class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        ret = []
        def run(l,r, p):
            if l == r == n:
                ret.append(p)
                return p
            print(p)
            if l < n:
                p += "("
                run(l+1,r,p)
                p = p[:-1]
            if r < l:
                p += ")"
                run(l,r+1,p)
                p = p[:-1]
            
            return p
        run(0,0,'')
        return ret



        
        