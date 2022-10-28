# https://www.acmicpc.net/problem/2839
# DP

N={0:0}
for i in range(1,int(input())+1):
  if i-5 in N and N[i-5]!=-1:
    N.setdefault(i, 0)
    N[i]+=N[i-5]+1
  elif i-3 in N and N[i-3]!=-1:
    N.setdefault(i, 0)
    N[i]+=N[i-3]+1
  else:
    N[i]=-1
print(N[len(N)-1])

# 처음부터 최소 갯수를 구해서 저장해서 재활용