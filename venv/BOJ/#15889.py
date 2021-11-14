N=int(input())
dist=list(map(int,input().split()))

if N==1:
    print("권병장님, 중대장님이 찾으십니다")
    exit()
else:
    for_dist = list(map(int, input().split()))
    max_dist=0
    for i in range(N-1):
        max_dist=max(max_dist,dist[i]+for_dist[i])

        if max_dist>=dist[i+1]:
            continue
        else:
            print("엄마 나 전역 늦어질 것 같아")
            exit()

    print("권병장님, 중대장님이 찾으십니다")


