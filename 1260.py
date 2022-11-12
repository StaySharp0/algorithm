# https://www.acmicpc.net/problem/1260
# DFS, BFS

def S(s):return map(int,s.split())
I=[*open(0)]
N,_,s=S(I[0])
M=[[0]*(N+1) for _ in range(N+1)]
for x in I[1:]:a,b=S(x);M[a][b]=1;M[b][a]=1
def D(R,s):
    R[str(s)]=0
    for i,x in enumerate(M[s]):
        if x and str(i) not in R:
            D(R,i)
R={};D(R,s)
print(' '.join(R.keys()))

R={}
R[str(s)]=0
k=0
while k<len(R):
    for i,x in enumerate(M[int([*R.keys()][k])]):
        if x and str(i) not in R:
            R[str(i)]=0
    k+=1
print(' '.join(R.keys()))


# def S(s):return map(int,s.split())
# I=[*open(0)];N,_,s=S(I[0]);M=[[0]*(N+1) for _ in range(N+1)]
# for x in I[1:]:a,b=S(x);M[a][b]=1;M[b][a]=1
# def D(R,s):
#     R[str(s)]=0
#     for i,x in enumerate(M[s]):
#         if x and str(i) not in R:D(R,i)
# R={};D(R,s)
# print(' '.join(R.keys()))
# R={};R[str(s)]=0;k=0
# while k<len(R):
#     for i,x in enumerate(M[int([*R.keys()][k])]):
#         if x and str(i) not in R:R[str(i)]=0
#     k+=1
# print(' '.join(R.keys()))
