class Solution:
    def plusOne(self, digits):
        num=[str(x) for x in digits]
        num=''.join(num)
        num=int(num)+1
        num=list(str(num))
        num=[int(x) for x in num]
        return num