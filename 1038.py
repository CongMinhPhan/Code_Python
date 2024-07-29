def tong(s,k):
    k=k+1
    if(k>1000):
        return -1
    s1=s[::-1]
    n=int(s)
    m=int(s1)
    l=n+m
    if l%7==0:
        return l
    s2=str(l)
    return tong(s2,k)

t=int(input())
while(t>0):
    t=t-1
    s=str(input())
    k=0
    print(tong(s,k))

