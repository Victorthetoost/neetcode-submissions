class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def expand(left,right):
            print(left,right, "before")
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left-=1
                right +=1
            print(left, right)
            return left,right 
        longest = ""
        num = 0
        for i in range(len(s)-1):
            l,r = expand(i,i)
            length = r-l +1
            if length > num:
                num = length
                longest = s[l:r+1]
            if(s[i] == s[i+1]):
                l,r = expand(i,i+1)
                length = r-l +1
                print("length", length,num)
                if length > num:
                    num = length
                    longest = s[l:r+1]
        return longest
