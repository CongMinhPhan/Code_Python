mod = 1e9 + 7
def poww(n,k):
    if (k == 1):
        return n
    x = poww(n, k / 2)
    if (k % 2 == 0):
        return (x * x) % mod
    else:
        return (((x * x) % mod) * n) % mod

n=int(input())
k=int(input())
print(poww(n, k)) 
