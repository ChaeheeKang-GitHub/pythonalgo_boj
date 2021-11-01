from itertools import permutations
N,M = map(int,input().split())
ar=[i for i in range(1,N+1)]

ans=list(permutations(ar,M))
for i in ans:
    print(' '.join((map(str,i))))