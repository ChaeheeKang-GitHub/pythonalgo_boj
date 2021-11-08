N,D=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
l=sorted(l)

dp=[i for i in range(D+1)]

for s,e,d in l:
    if e>D:
        continue
    if dp[e]>dp[s]+d:
        dp[e]=dp[s]+d
        for i in range(e+1,D+1):
            if dp[i]>dp[i-1]+1:
                dp[i]=dp[i-1]+1
            else:
                break
print(dp[D])