# https://www.acmicpc.net/problem/1780
# 1992, 2630 문제와 유사

I=[x.split()for x in[*open(0)][1:]]
T=[(x,y) for x in range(3) for y in range(3)]
t=[0,0,0]
def R(x,y,n):
    m=I[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if I[i][j]!=m:
                for a,b in T:R(x+a*n//3,y+b*n//3,n//3)
                return
    for x in[-1,0,1]: 
        if int(m)==x:t[x]+=1
R(0,0,len(I))
for x in[-1,0,1]:print(t[x])
