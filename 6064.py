# https://www.acmicpc.net/problem/6064
for _ in[*open(0)][1:]:
    m,n,x,y=map(int,_.split());x+=x*m
    while x<=m*n:
        if (x-y)%n==0:print(x);break
        x+=m
    else:print(-1)

# 최소공배수가 마지막 해-> 시간초과

# 1 1:1
# 2 2:2
# 3 3:3
# 4 4:4
# 5 5:5
# 6 6:6
# 7 7:7
# 8 8:8
# 9 9:9
# 10 10:10
# 11 1:11
# 12 2:12
# 13 3:1
