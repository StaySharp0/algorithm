# https://www.acmicpc.net/problem/1978
# 소수

def fn(n):
  n=int(n)
  for i in range(2,n):
    if n%i==0: return 0
  return 0 if n==1 else 1
print(sum([fn(n) for n in [*open(0)][1].split()]))