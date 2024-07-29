s1 = [i.lower() for i in input().split(' ')]
s2 = [i.lower() for i in input().split(' ')]
m1={}
m2={}
m3={}
for i in s1:
    m1[i]=1
    m2[i]=1
for i in s2:
    m1[i]=1
    m3[i]=1

for i in sorted(list(m1)):
    print(i, end = ' ')
print()
for i in sorted(list(m2)):
    if i in m3:
        print(i, end = ' ')
