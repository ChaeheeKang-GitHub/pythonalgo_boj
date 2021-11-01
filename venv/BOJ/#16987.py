N=int(input())
d=[0]*N
w=[0]*N

for i in range(N):
    d[i],w[i] = map(int,input().split())
res=0
def solve(idx,eggs):
    global res
    if idx==N:
        cnt=0
        for i in range(N):
            if eggs[i]<=0:
                cnt+=1
            if cnt> res:
                res=cnt
            return
    if effs[idx]>0:
        for i in range(N):
            flag=False

solve(0,d)
print(res)