N=int(input())
l=[]
cnt=0
for i in range(N):
    s,e=map(int,input().split())
    l.append((s,e))

l.sort()
ps,pe=l[0][0],l[0][1]

for i in range(1,N):
    s,e=l[i][0],l[i][1]
    if s<=pe:
        pe=max(pe,e)
    else:
        cnt+=pe-ps
        ps,pe=s,e
cnt+=pe-ps
print(cnt)