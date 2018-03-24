class Solution:
    def addBinary(self, a, b):
        a=int(a,2)
        b=int(b,2)
        ans=a+b
        ans=bin(ans)
        ans=ans[2:]
        return ans