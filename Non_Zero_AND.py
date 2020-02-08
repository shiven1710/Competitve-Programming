x=int(input())
n=list(map(int,input().split()))
q=int(input())
l=[]
t=False
for i in range(q):
    l.append(list(map(int,input().split())))
for i in range(len(l)):
    left=l[i][0]-1
    right=l[i][1]
    for j in range(left,right):
        if(n[j]&n[j+1]==1):
            t=True
    if(t):
        print("YES")
    else:
        print("NO")