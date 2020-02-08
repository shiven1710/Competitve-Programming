x=int(input())
l=list(map(int,input().split()))
l.sort()
flag=True
for i in range(len(l)-1):
    if(abs(l[i]-l[i+1])!=1):
        flag=False
if(flag):
    print("YES")
else:
    print("NO")