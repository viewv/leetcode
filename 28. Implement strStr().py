class Solution:
    def strStr(self, haystack, needle):
        n=len(needle)
        N=len(haystack)
        step=N-n
        if step==0:
            if haystack==needle:
                return 0
            else:
                return -1
        for x in range (0,step+1):
            temp=haystack[x:x+n]
            if temp==needle:
                return x
        return -1