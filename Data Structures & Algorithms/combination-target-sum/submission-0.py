class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = []
        def run(temp,n):
            
            if sum(temp) == target:
                final.append(temp[:])
            for num in range(n,len(nums)):

                if (sum(temp)+nums[num] <= target):
                    temp.append(nums[num])
                    run(temp,num)
                    temp.pop()
            return final
        
        final = run([],0)
        return final