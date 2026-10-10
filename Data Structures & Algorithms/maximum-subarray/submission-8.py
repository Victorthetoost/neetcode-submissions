class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = [0]
        ret[0] = nums[0]
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        mem  = {}
        def run(n):
            sums = 0
            if (n ==0):
                return nums[0]
            
            if n in mem:
                return mem[n]

            mem[n] = max(nums[n], nums[n]+run(n-1))
            if mem[n] > ret[0]:
                ret[0] = mem[n]
            return mem[n]  
        
        run(len(nums)-1)
        return ret[0]