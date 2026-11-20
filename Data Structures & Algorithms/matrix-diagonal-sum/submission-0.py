class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        j = 0
        ret = 0
        while i< len(mat):
            ret += mat[i][j]
            i+=1
            j+=1
        i = 0
        j = len(mat)-1
        while i< len(mat):
            if i!= j:
                ret += mat[i][j]
            i+=1
            j-=1
        return ret