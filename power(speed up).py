import math

def power(x,n):
    y=1
    while True:
        t=n%2
        n=math.floor(n/2)
        if t==1:
            y=y*x
        if n==0:
            break
        x=x*x
    return y

nums=input()
nums=nums.split()
x=int(nums[0])
n=int(nums[1])
print(power(x,n))