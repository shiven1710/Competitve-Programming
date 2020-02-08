try:
    t=int(input())
    for i in range(t):
        s=input()
        s=s.split(" ")
        s=[int(i) for i in s]
        f=input()
        f=f.split(" ")
        f=[int(i) for i in f]
        time=0
        if(s[2]>=s[1] and s[2]<=f[0]):
            time=(f[0]-s[2])+s[3]+(f[0]-s[1])
        elif(s[2]>=s[1] and s[2]>f[0]):
            if(f[0]<=s[1]):
                for k in f:
                    if(k<=s[1]):
                        tem=k
                time=(s[2]-tem)+s[3]+(s[1]-tem)
            else:
                time=(s[2]-f[0])+s[3]+(f[0]-s[1])
        elif(s[1]>=s[2] and s[1]<=f[0]):
            time=(f[0]-s[2])+s[3]+(f[0]-s[1])
        elif(s[1]>=s[2] and s[1]>f[0]):
            if(f[0]<=s[1]):
                for k in f:
                    if(k<=s[1]):
                        tem=k
                time=(tem-s[2])+s[3]+(s[1]-tem)
            else:
                time=(f[0]-s[2])+s[3]+(f[0]-s[1])
        print(time)
except:
    pass