class Solution:
    def longestPalindrome(self, s):
        maxlength=1
        N=len(s)
        if N<=0:
            return ""
        rstr=s[0]
        for x in range(0,N):
            tempa=s[x]
            for y in range(N-1,x,-1):
                tempb=s[y]
                if tempa==tempb:
                    temp=s[x:y+1]
                    if temp==temp[::-1] and len(temp)>maxlength:
                        rstr=temp
                        maxlength=len(temp)
                        break
        return rstr