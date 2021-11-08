N=int(input())
M=int(input())

l=[[] for _ in range(N+1)]
for i in range(M):
    s,e,w=map(int,input().split())
    l[s].append([e,w])

rs,re=map(int,input().split())

