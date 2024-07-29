def nt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def kt(s):
    for i in range(0,len(s)):
        if(nt(i)):
            if(s[i]!="2" and s[i]!="3" and s[i]!="5" and s[i]!="7"):
                return 0
        else:
            if(s[i]=="2" or s[i]=="3"or s[i]=="5"or s[i]=="7"):
                return 0

    return 1
t = int(input())
while t > 0:
    t -= 1
    s=str(input())
    if kt(s)==1 :
        print("YES")
    else:
        print("NO")
    