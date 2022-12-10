# https://www.acmicpc.net/problem/1043
# 거짓말
# 조합 
I=lambda:[*map(int,input().split())]
n,m=I()
c,*k=I()
k={*k}
p=[{*I()[1:]}for _ in range(m)]
for i in p:
    for i in p:
        if i&k:k|=i
r=0
for i in p:
    if not i&k:r+=1
print(r)
# 한바퀴 더 돌려서 아는 사람 목록을 갱신 해줘야함(마지막 케이스 참고)
