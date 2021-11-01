X=int(input())
cnt=1

while X!=1:
    cnt+=X%2
    X//=2

print(cnt)

