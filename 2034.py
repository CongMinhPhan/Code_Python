s=input()
l=len(s)
m = {}
for i in range(0,l,2):
    s2=""
    s2=s2+s[i]+s[i+1]
    if s2 in m:
        m[s2]+=1
    else:m[s2]=1
    
