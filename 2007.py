while(1):
    a=[int(x) for x in input().split()]
    x=x+len(a)
    t=0
    for i in a:
        if(i%42!=0):
            t=t+1
    if x==10:
        break
print(t)