
m={}
n,k=[int(x) for x in input().split() ]
a=[int(x) for x in input().split() ]
b=[0]*(k+1)
for i in a:
    m[i]=1
a=sorted(list(m))
print(a)
def Try(p):
    if p==k:
        for i in range(1,k+1):
            print(a[b[i]-1],end="")
            print()
    for i in range(b[p]+1,n+1):
            b[p+1]=1
            Try(p+1)
Try(0)

