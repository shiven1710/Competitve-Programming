def fact_string(x):
    f=1
    for i in range(1,x+1):
        f*=i
    return str(f)
def count_last_zeros(str):
    c=0
    rev=spacify(reverse(str)).split()
    for i in rev:
        if(i=='0'):
            c+=1
        else:
            break
    return c
def reverse(str):
    rev=""
    for i in str:
        rev=i+rev
    return rev
def spacify(str):
    space=""
    for i in str:
        space=space+i+" "
    return space
n=int(input())
for i in range(1,(n*5)+1):
    num=fact_string(i)
    nez=count_last_zeros(num)
    if(nez==n):
        print(i)
        break
