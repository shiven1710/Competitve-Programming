import sys
age=list(map(int,input().split()))
#age=[1,2,3,4,5,6]
pos=0
ns=0
i=0
for a in age:
    if(a<1 or a>9):
        print(ns)
        sys.exit(0)
while i < len(age):
    j=i+1
    while j < len(age):
        if(age[i]==age[j]):
            pos=j+1
        j=j+1
    if(pos!=0):
        ns=ns+1
        i=pos-1
        pos=0
    else:
        i=i+1
        if(i!=len(age)):
            ns=ns+1
print(ns)
