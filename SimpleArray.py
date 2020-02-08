t=int(input())
n=[]
l=[]
for i in range(t):
    n.append(int(input()))
    l.append(list(map(int,input().split())))
for i in l:
    m=i[0]-i[1]
    for j in i:
        c=0
        for k in i:
            if(j==k):
                c+=1
            k2=j-k
            if(k2>m):
                m=k2
        if(c>=len(i)//2):
            gt=j
    print(m,gt)
    