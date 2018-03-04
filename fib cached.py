import profile
class cached:
    def __init__(self,fn):
        self.fn=fn
        self.cache={}
    def __call__(self,*args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = self.fn(*args)
            return self.cache[args]
@cached
def fib(n):
    a,b=0,1
    for x in range(0,n):
        a,b=b,a+b
    return a

def fib_seq(n):
    seq = []
    for x in range(0,n+1):
        seq.append(fib(x))
    return seq

seq=fib_seq(1000)
for x in seq:
    print(x)