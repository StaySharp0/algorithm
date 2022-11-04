# https://www.acmicpc.net/problem/9095
# DP
R=[0,1,2,4]
for x in [*map(int,[*open(0)][1:])]:
  l=len(R)
  if x>=l:
    for i in range(l, x+1): R.append(sum(R[i-3:i]))
  print(R[x])

# N 조합의 수 
# = 1+(N-1) 조합의 수
# = 2+(N-2) 조합의 수
# = 3+(N-3) 조합의 수