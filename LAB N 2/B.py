def bfSum(a,A,b,B):
    la,ra=0,a 
    lb,rb=0,b
    res=[]*(a+b)
    while la<ra and lb<rb:
        if A[la]<B[lb]:
            res.append(A[la])
            la+=1
        else:
            res.append(B[lb])
            lb+=1

    while la<ra:
        res.append(A[la])
        la+=1
    while lb<rb:
        res.append(B[lb])
        lb+=1


    print(str(res)[1:-1].replace(",",""))
a=int(input())
A=list(map(int,input().split()))
b=int(input())
B=list(map(int,input().split()))
res=bfSum(a,A,b,B)

