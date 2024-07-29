def tong(n):
    l=list(n)
    res=0
    for i in range(0,len(l)):
        res=res+int(l[i])
    return res
def tong2(n):
    l=list(n)
    res=0
    for i in range(0,len(l)):
        a=int(l[i])
        if(i==0):
            res=res-a
        res=res+a
    return res
s=str(input())
n=int(s)
t=0
if(n<0):
    n=abs(n)
    if(n<10):
        t=1
    while(int(n)>=10):
        t=t+1
        m=str(n)
        n=int(tong2(m))
else:
    while(int(n)>=10):
        t=t+1
        m=str(n)
        n=int(tong(m))
print(t)