#def check(a):
#    for i in a:
#        if(i!=0):
#            return False
#    return True
#minions=list(map(int,input().split()))
#minions.sort()
#i=0
#j=len(minions)-1
#while(i<len(minions)-1):
#    if(minions[i]<=0):
#        i=i+1
#    if(i==len(minions)-1):
#        break
#    if(minions[j]>minions[i] and minions[i]!=0):
#        minions[j]-=1
#        minions[i]-=1
#    elif(minions[j]==minions[i] and minions[i]!=0):
#        if(j!=i):
#            minions[j]-=1
#            minions[i]-=1
#            if(minions[j]==0):
#                j=j-1
#        else:
#            break
#    else:
#        j=len(minions)-1
#        minions.sort()
#    if(j==0):
#        break
#    if(minions[i]==0):
#        i=i+1
#if(check(minions)):
#    print("Yes")
#else:
#    print("No")
def check(a):        
    for i in range(len(minions)):
        if(minions[i]!=0):
            return False
            break
    return True
minions=list(map(int,input().split()))
minions.sort(reverse=True)
while(minions[0]!=0 and minions[1]!=0):
    for i in range(1,len(minions)):
        print(minions)
        if(minions[0]>0 and minions[i]>0):
            minions[0]=minions[0]-1
            minions[i]=minions[i]-1
        if(minions[0]==0):
            minions.sort(reverse=True)
            break
print(minions)
if(check(minions)):
    print("Yes")
else:
    print("No")