# https://www.acmicpc.net/problem/5525

# 50점
# T=int
# I=input
# n=T(I())
# a=2*n+1
# m=T(I())
# s=I()
# r=0
# for i in range(m-a+1):
#     if s[i:i+a]=='IO'*n+'I':r+=1
# print(r)

# 100점
T=int
I=input
n=T(I())
m=T(I())
s=I()
r=c=0
i=1
while i < m-1:
    if s[i-1:i+2]!='IOI':i+=1;c=0;continue
    i+=2;c+=1
    if c==n:c-=1;r+=1
print(r)
