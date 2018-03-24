class Solution:
    def isPowerOfTwo(self, n):
        n=bin(n)
        n=n[2:]
        n=list(n)
        for x in range(1,len(n)):
            if n[x]=='1':
                return False
        return True
