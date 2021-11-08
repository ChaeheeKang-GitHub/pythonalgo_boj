N=int(input())
l=list(map(str,input()))

dp=[10000000001]*N
dp[0]=0

for i in range(N):
    now=l[i]
    right=''
    if now == 'B':
        right='O'
    elif now =='O':
        right='J'
    else:
        right='B'

    for j in range(i+1,N):
        if l[j]==right:
            dp[j]=min(dp[j],dp[i]+(j-i)*(j-i))
ans=dp[N-1]
if ans==10000000001:
    print(-1)
else:
    print(ans)