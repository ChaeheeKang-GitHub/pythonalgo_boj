N=int(input())
x=['1','2','3']
total = True

def btk(index,result):
    global total
    if total:
        if len(result)==N:
            print(result)
            total=False
            return
        for i in range(3):
            flag=True
            result+=x[i]

            for j in range(1,int(index/2)+1):
                if result[-j-j:-j]==result[-j:]:
                    result=result[:-1]
                    flag=False
            if flag:
                btk(index+1,result)
    else:
        return

btk(1,'')
