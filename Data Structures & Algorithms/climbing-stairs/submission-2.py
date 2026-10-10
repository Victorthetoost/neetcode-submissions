class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        mem = {}
        def next_step (n,mem):
            if n == 1:
                return 1
            if n ==2 :
                return 2
            if n in mem:
                return mem[n]
            mem[n] = next_step(n-1,mem) + next_step(n-2,mem)
            return mem[n]
        
            
        
        return next_step(n,mem)