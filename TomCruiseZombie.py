# import itertools
# def sublist(a,n):
#     return list(map(list,itertools.combinations(a,n)))
# def sum(a):
#     s=0
#     for i in a:
#         s=s+i
#     return s
# n=int(input())
# l=list(map(int,input().split()))
# nl=[]
# for i in range (1,n+1):
#     nl.append(sublist(l,i))
# print(nl)
# x,y=0,0
# for i in range(n):
#     for j in nl[i]:
#         if(sum(j)%2==0):
#             x=x+1
#         else:
#             y=y+1
# print(x,y)
x=int(input())
l=list(map(int,input().split()))
total=(2**x)-1
count_even=0
x,y=0,0
for i in l:
    if(i%2==0):
        count_even+=1
if(count_even==len(l)):
    x=total
    print(x,y)
else:
    x=total//2
    y=total-x
    print(x,y)