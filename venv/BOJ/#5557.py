N=int(input())
l=list(map(int,input().split()))

dp=[[0]*21 for _ in range(N)]
first=l.pop(0)
last=l.pop()
dp[1][first]=1

for i in range(1,N-1):
    x=l.pop(0)
    for j in range(21):
        if(0<=j+x<=20):
            dp[i+1][j+x]+=dp[i][j]
        if(0<=j-x<=20):
            dp[i+1][j-x]+=dp[i][j]
print(dp[N-1][last])