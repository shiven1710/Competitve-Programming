c=int(input())
nr=c*2-1
count=-1
bt=0
for i in range(nr):
    if(count==nr):
        break
    count=count+2
    bt=bt+count
for i in range(nr):
    if(count==1):
        break
    count=count-2
    bt=bt+count
print(bt)