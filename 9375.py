# https://www.acmicpc.net/problem/9375
from collections import Counter as C
T=int
I=input
R=range
for _ in R(T(I())):
    w,c=[],1
    for _ in R(T(I())):w.append(I().split()[1])
    for v in C(w).values():c*=v+1
    print(c-1)

# (옷 갯수 + 안입은 경우)*... 종류 수 만큼 계산 -1(모두다 안입은 경우 제외)
