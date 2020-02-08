t=int(input())
n=[]
for i in range(t):
    n.append(int(input()))
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
for i in n:
    sum=0
    for j in range(1,i+1):
        bef=j-1
        aft=i-j
        if(bef==0):
            sum+=fact(aft)
        elif(aft==0):
            sum+=fact(bef)
        elif(bef==1 and aft==1):
            sum+=1
        else:
            sum+=fact(bef)+fact(aft)
    print(sum%((10**9)+7))