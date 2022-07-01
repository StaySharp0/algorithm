# https://www.acmicpc.net/problem/11866
# 구현 자료구조 큐
N,K=map(int,input().split())
A=[str(i+1) for i in range(N)]
R=[]
while len(A) > 0:
  T=K-1 if K-1 < len(A) else (K-1)%len(A)
  R.append(A[T])
  A=A[T+1:]+A[:T]
print('<'+', '.join(R)+'>')