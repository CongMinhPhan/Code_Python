t=int(input())
while(t>0):
    t=t-1
    s=str(input())
    l=list(s)
    l.sort()
    k=0
    for i in range(0,len(l)):
        if(l[i].isdigit()==1):
            k=k+int(l[i])
        if(l[i].isdigit()==0):
            print(l[i],end="")
    print(k)
