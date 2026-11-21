class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = {}
        last = len(nums)-1
        i = 0
        while i in range(len(nums)):

            if nums[i] in found:
                print("got here")
                if found.get(nums[i]) == 2:
                    print(nums, "before")
                    nums[i:] = nums[i+1:]
                    print(nums, "after")
                    last -= 1
                    continue
                else:
                    found[nums[i]] = 2
            else:
                print("did this")
                found[nums[i]] = 1
            print (found)
            i += 1
        new = nums[:last+1]
        print(new, "new")
        return len(new)
