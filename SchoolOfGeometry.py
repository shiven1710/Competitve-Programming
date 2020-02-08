t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    sum=0
    for i in range(n):
        if(a[i]<b[i]):
            sum=sum+a[i]
        else:
            sum=sum+b[i]
    print(sum)
