t=int(input())
ans=[]
for i in range(t):
    nk=list(map(int,input().split()))
    num=list(map(int,input().split()))
    r=0
    for i in num:
        if(i%nk[1]>0):
            r+=i%nk[1]
    ans.append((r%nk[1]))
for i in ans:
    print(i,end=" ")