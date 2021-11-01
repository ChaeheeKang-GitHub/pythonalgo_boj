N=int(input())
game=[list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0]=1

for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1:
            print(dp[i][j])
            break
        cnt=game[i][j]  #이동할 수 있는 거리 cnt
        #오른쪽
        if j+cnt<N:
            dp[i][j+cnt]+=dp[i][j]
        #아래쪽
        if i+cnt<N:
            dp[i+cnt][j]+=dp[i][j]

