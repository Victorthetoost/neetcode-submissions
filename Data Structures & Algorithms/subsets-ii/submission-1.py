class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = set()
        nums.sort()
        def recur(index, path):
            if index == len(nums):
                path = tuple(path)
                out.add(path)
                return
            if index == len(nums) :
                return

            path.append(nums[index])
            recur(index +1, path)
            path.pop()

            recur(index +1, path)
        recur (0, [])
        return list(out)



