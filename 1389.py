# https://www.acmicpc.net/problem/1389
# 그래프, 플루이드-워셜, DFS
# def S(s):
#     return map(int,s.split())
# I=[*open(0)]
# N,_=S(I[0])
# M=[[0]*N for _ in range(N)]
# 
# for _ in I[1:]:
#     x,y=S(_);
#     M[x-1][y-1]=1
#     M[y-1][x-1]=1
# r=range
# for k in r(N):
#     for x in r(N):
#         for y  in r(N):
#             A=M[x][k]
#             B=M[k][y]
#             if A!=0 and B!=0:
#                 M[x][y]=min(M[x][y],A+B) if M[x][y] else A+B
# R,r=0,0
# for i,_ in enumerate(M):
#     _[i]=0
#     if -sum(_)>R or R==0:
#         R=-sum(_)
#         r=i
# print(r+1)


def S(s):return map(int,s.split())
I=[*open(0)];N,_=S(I[0]);M=[[0]*N for _ in range(N)]
for _ in I[1:]:x,y=S(_);M[x-1][y-1]=1;M[y-1][x-1]=1
r=range
for k in r(N):
    for x in r(N):
        for y  in r(N):
            A=M[x][k];B=M[k][y]
            if A!=0 and B!=0:
                M[x][y]=min(M[x][y],A+B) if M[x][y] else A+B
R,r=0,0
for i,_ in enumerate(M):
    _[i]=0
    if -sum(_)>R or R==0:R=-sum(_);r=i
print(r+1)

