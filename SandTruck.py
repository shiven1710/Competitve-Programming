n=int(input())
t=n
num=0
num2=0
truck_size=list(map(int,input().split()))
truck_size.sort()
i=len(truck_size)-1
#QUESTION 3
while(n>0):
    if(n%truck_size[i]==0):
        num=num+(n//truck_size[i])
        n=n-((n//truck_size[i])*truck_size[i])
    else:
        if(n<truck_size[i]):
            i=i-1
            continue
        num=num+(n//truck_size[i])
        n=n-((n//truck_size[i])*truck_size[i])
#QUESTION 5
for i in truck_size:
    if(t%i==0):
        num2=t//i
    if(num2<num):
        num=num2
print(num)