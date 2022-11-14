# https://www.acmicpc.net/problem/1620
I=[_[:-1]for _ in[*open(0)]]
N,M=map(int,I[0].split())
R={}
for i,s in enumerate(I[1:N+1]):i+=1;R[s]=i;R[str(i)]=s
for s in I[N+1:]:print(R[s])
