class Solution:
    def rob(self, nums: List[int]) -> int:
        house = {}

        def rob (n,l):
            # rob house or skip

            if n in house:
                return house[n]
            if (n < l):
                return 0
            if (n == l):
                return nums[l]
            
            house[n] = max(rob(n-1,l), nums[n] + rob(n-2,l))
            print(house)
            
            return house[n]
        
        a = rob(len(nums)-1, 1)
        print(a)
        house = {}
        b = rob(len(nums)-2, 0)
        print(b)
        n = max(a,b)
        if len(nums) == 1:
            return nums[0]
        return n

