n, k = [int(x) for x in input().split()]
m = {}
for z in range(n) :
    s = ''
    for i in input().lower() + ' ' :
        if not(i.isalpha()) and not(i.isdigit()) :
            if(s != '') :
                if s in m : m[s] += 1
                else : m[s] = 1
                s = ''
        else : s += i
m = sorted(m.items(), key = lambda x: (-x[1], x[0]))
for i in m :
    if i[1] >= k : print(i[0], i[1])