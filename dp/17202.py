# https://www.acmicpc.net/problem/17202
# 핸드폰 번호 궁합
# DP
R=range
c=[0]*16
for s in R(2):
    for i,v in enumerate(input()):c[2*i+s]=int(v)
while len(c)>2:
    l=len(c)-1;t=[0]*l
    for i in R(l):t[i]=(c[i]+c[i+1])%10
    c=t
print(*c,sep="")
