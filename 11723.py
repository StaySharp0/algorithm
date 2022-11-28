# https://www.acmicpc.net/problem/11723
# 비트마스킹
import sys
T=int
I=sys.stdin.readline
S=[False for _ in range(31)]
for _ in range(T(I())):
    c,*n=I().split()
    if c=='all':S=[True for _ in range(31)]
    elif c=='empty':S=[False for _ in range(31)]
    else:
        n=T(n[0])
        if c=='add':S[n]=True
        elif c=='remove':S[n]=False
        elif c=='check':print(1 if S[n]else 0)
        else:S[n]=not S[n]

# tip: 앞의 글자가 다른 것 활용
# import sys
# S=0
# input()
# for l in sys.stdin:
#  c,*A=l.split()
#  x,y=c[2],1<<int(*A)
#  if'd'==x:S|=y
#  if'm'==x:S&=~y
#  if'e'==x:print(+(S&y>0))
#  if'g'==x:S^=y
#  if'l'==x:S=(1<<21)-1
#  if'p'==x:S=0
