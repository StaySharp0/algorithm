# https://www.acmicpc.net/problem/1074
# 분할정복
N,r,c=map(int,input().split())
R=0
while N!=0:
    N-=1;n=2**N
    if r<n:
        if c>=n:R+=n*n;c-=n
    elif c<n:R+=n*n*2;r-=n
    else:R+=n*n*3;r-=n;c-=n
print(R)

# 
# 1. 어느 4분면에 있는지 찾기 
# 2. 각 기준점 업데이트
# 3. 사분면에서의 r,c 위치 조정
