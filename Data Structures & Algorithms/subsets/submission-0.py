class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def recur(index, path):
             #base case:
            if (index == len(nums)):
                #append the path and return 
                out.append(path[:])
                return
            
            # add case
            path.append(nums[index])
            recur(index +1, path)
            # base case should have already added it atp
            path.pop()
            #skip case
            recur(index +1, path)
        recur (0, [])
        return out
