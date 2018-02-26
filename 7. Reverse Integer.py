class Solution:
    def reverse(self, x):
        if x <0:
            x=-1*x
            x=str(x)
            x=x[::-1]
            x=-1*int(x)
        else:
            x=str(x)
            x=x[::-1]
            x=int(x)
        if x>(2**31-1) or x<(-1*2**31):
            '''
            Assume we are dealing with an environment 
            which could only hold integers within the 32-bit 
            signed integer range. For the purpose of this problem,
            assume that your function returns 0 
            when the reversed integer overflows.
            emmmm python :(,:)
            '''
            return 0
        else:
            return x
            