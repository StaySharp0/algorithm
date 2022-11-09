# https://www.acmicpc.net/problem/1012
M=[-1,0,1,0,0,1,0,-1]
def R(I,i,j):
    if I[i][j]==0:return 0
    V=[(i,j)]
    while len(V):
        i,j=V.pop();I[i][j]=0
        for _ in range(4):
            a,b=M[_::4];y=i+a;x=j+b
            if x<0 or y<0 or x>X or y>Y:continue
            if I[y][x]:V.append((y,x)) 
    return 1
E=0
V=[]
for x in [*open(0)][1:]:
    x,y,*a=map(int,x.split())
    if len(a):E=a[0];V=[];X,Y=x-1,y-1;I=[[0]*x for _ in range(y)];
    else:V.append((y,x));I[y][x]=1
    if len(V)==E:
        c=0
        for i,j in V:c+=R(I,i,j)
        print(c)

# unpacking tip: * 붙이기
