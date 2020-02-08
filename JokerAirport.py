def count_segment(n):
    c=0
    for i in range(n):
        for j in range(n,0,-1):
            t=j
            if(i+j==n):
                c=c+1
            if(i==j):
                break
    if(n%2==0):
        return c-1
    return c        
xy=list(map(int,input().split()))
x=xy[0]
y=xy[1]
sum=0
c=count_segment(x)
print(c)