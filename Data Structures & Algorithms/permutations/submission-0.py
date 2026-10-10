class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []


        def recur(path):
            if (len(path) == len(nums)):
                out.append(path[:])
                return out
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    recur(path)
                    path.pop()
            return out
        
        out = recur([])
        return out

                