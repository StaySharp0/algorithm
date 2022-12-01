# https://www.acmicpc.net/proble/5430
from collections import deque as D
I=input
t=int(I())
for _ in range(t):
    r=0;p=I();I();x=I()[1:-1];x=D(x.split(','))if x else D()
    for c in p:
        if c=='R':r+=1
        if c=='D':
            if not x:print('error');break
            if r%2:x.pop()
            else:x.popleft() 
    else:
        if r%2:x.reverse()
        print('['+','.join(x)+']')
