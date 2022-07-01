# https://www.acmicpc.net/problem/1018
# 브루트포스
I=[*open(0)]
N,M=map(int, I[0].split())
I=[[u for u in _][:-1] for _ in I[1:]]
R=[]

def F(B,C):
  R=0
  for r,_ in enumerate(B):
    for c,u in enumerate(_):
      if u!=C[(r+c)%2]:
        R+=1
  return R

for i in range(N-7):
  for j in range(M-7):
    B=[r[j:j+8] for r in I[i:i+8]]
    R.append(F(B,'WB'))
    R.append(F(B,'BW'))

print(min(R))
