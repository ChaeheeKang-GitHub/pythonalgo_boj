N=int(input())

dp= [0]*101
dp[1]=1
dp[2]=2
dp[3]=3

if N<=3:
    print(dp[N])
else:

    for i in range(1,N+1):
        dp[i]=dp[i-1]+1     #그냥 A를 누른다고 했을때
        for x in range(i-3,0,-1):
            tmp=dp[x]*(i-x-1)
            dp[i]=max(dp[i],tmp)
    print(dp[N])