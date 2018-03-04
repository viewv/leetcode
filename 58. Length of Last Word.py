class Solution:
    def lengthOfLastWord(self, s):
        s=s.split()
        if len(s)==0:
            return 0
        return len(s[-1])