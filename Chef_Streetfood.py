# cook your dish here
try:
    t = int(input())
    n = int(input())
    s = input()
    s = s.split(" ")
    s = [int(i) for i in s]
    profit = (s[1]//(s[0]+1))*s[2]
    for i in range(t):
        for j in range(n-1):
            s = input()
            s = s.split(" ")
            s = [int(i) for i in s]
            
            p = (s[1]//(s[0]+1))*s[2]
            if(profit<p):
                profit = p
            if(j == n-2):
                print(profit)
                n = int(input())
                s = input()
                s = s.split(" ")
                s = [int(i) for i in s]
                profit = (s[1]//(s[0]+1))*s[2]
                if(n == 1):
                    print(profit)                
except:
    pass
