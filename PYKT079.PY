t=int(input())
while(t>0):
    n = int(input())
    m = {}
    s = 0
    a = [int(x) for x in input().split()]
    for i in a :
        m[i] = 1
    Min = min(a)
    Max = max(a)
    for i in range(Min, Max) :
        if not(i in m) : s += 1
    print(m)
    t=t-1