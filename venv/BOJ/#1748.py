N=int(input())
l=len(str(N))
ans=0

if l==1:
    ans=1*N
else:
    for i in range(l-1):
        ans+=(i+1)*9*10**i
    ans+=l*(N-(10**(l-1)-1))
print(ans)