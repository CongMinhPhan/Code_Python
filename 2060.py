MOD=1e9+7

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
def lcm(a,b):
    m=int(a*b/gcd(a,b))
    return m
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    m=int(lcm(a,b))
    s=1
    for i in range(a,b+1):
        s=s*i
    