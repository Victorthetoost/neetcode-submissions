class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #go from max to 0
        goal = len(nums)-1
        i = len(nums)-1
        while i >= 0:
            print(i, goal, "reach", nums[i]+i)
            if i + nums[i] >= goal:
                goal = i
            i -= 1
        if i == -1 and goal == 0:
            return True
        else:
            return False
