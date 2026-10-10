class Solution:
    def rob(self, nums: List[int]) -> int:
        house = {}

        def rob (n):
            # rob house or skip

            if n in house:
                return house[n]
            if (n < 0):
                return 0
            if (n == 0):
                return nums[0]
            
            house[n] = max(rob(n-1), nums[n] + rob(n-2))
            
            
            return house[n]
        
        rob(len(nums)-1)
        
        if house: 
            return max(house.values()) 
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            return 0

