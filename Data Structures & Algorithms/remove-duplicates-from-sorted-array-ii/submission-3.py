class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = {}
        last = len(nums)-1
        i = 0
        while i in range(len(nums)):

            if nums[i] in found:
                if found.get(nums[i]) == 2:
                    nums[i:] = nums[i+1:]
                    last -= 1
                    continue
                else:
                    found[nums[i]] = 2
            else:
                found[nums[i]] = 1
            i += 1
        new = nums[:last+1]
        return len(new)
