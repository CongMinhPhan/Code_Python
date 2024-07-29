
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s=input().split()
    l=[]
    for i in range(0,len(s)):
        a=int(s[i])
        l.append(a)
    d=dict.fromkeys(l)
    l1=list(d)
    res=0
    l1.sort()
    for i in range(0,len(l1)):
        b=l.count(l1[i])
        if(b>n/2):
            res=max(res,b)
    ok=0
    for i in range(0,len(l1)):
        b=l.count(l1[i])
        if(l.count(l1[i])==res):
            print(l1[i])
            ok=1
            break
    if(ok==0):
        print("NO")

