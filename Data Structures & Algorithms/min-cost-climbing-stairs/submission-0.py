class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}

        def step(n):
            if n in mem:
                return mem[n]

            if n < 2:
                return cost[n]

            mem[n] = cost[n] + min(step(n - 1), step(n - 2))
            return mem[n]

        return min(step(len(cost) - 1), step(len(cost) - 2))