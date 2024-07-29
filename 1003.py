s=str(input())
if(len(s)%2==1):
    k=len(s)-1
else:
    k=len(s)
b={}
for i in range(0,k,2):
    k=int(s[i])*10+int(s[i+1])
    if k in b:
        b[k]+=1
    else:
        b[k]=1
l=list(b)
l.sort()
for i in range(0,len(l)):
    print(l[i],end=" ")