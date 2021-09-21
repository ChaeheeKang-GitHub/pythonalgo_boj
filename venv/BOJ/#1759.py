from itertools import combinations

L,C=map(int,input().split())
cipher=list(input().strip().split())

cipher.sort()
moum = ['a', 'e', 'i', 'o', 'u']
a=list(combinations(cipher,L))

for i in a:
    answer=""
    flag1,flag2=0,0

    for check in i:
        if check in moum:
            flag1=1
        else:
            flag2+=1
    if flag1==1 and flag2>=2:
        print(*i,sep='')


