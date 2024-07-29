def check(s) :
    if len(s) < 3 : return False
    l=list(s)
    a=max(l)
    for i in range(1,len(l)):
        if (i<l.index(a) and l[i]<=l[i-1]) or (i>l.index(a) and l[i]>=l[i-1]):
            return 0
    return 1
   
t = int(input())
for i in range(t) :
    s=str(input())
    if check(s) == 1 : print("YES")
    else : print("NO")   