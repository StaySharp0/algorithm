# https://www.acmicpc.net/problem/17219
R={}
for l in[*open(0)][1:]:
  k,v,*_=l.split()+['']
  if v:R[k]=v
  else: print(R[k])