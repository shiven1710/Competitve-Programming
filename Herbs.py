x=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)-1):
    if(a[i]!=a[i+1]):
        c=c+1
        break
if(c==0):
    print(a[0])
else:
    sum=a[len(a)-1]
    for i in range(len(a)-1,0,-1):
        if(a[i]>a[i-1]):
            sum=sum+a[i-1]
        else:
            if(a[i]-1<0):
                a[i-1]=0
            else:
                a[i-1]=a[i]-1
                sum=sum+a[i-1]
    print(sum)
