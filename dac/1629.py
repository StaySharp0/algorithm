# https://www.acmicpc.net/problem/1629
# 곱셈
# divide and conquer
a,b,c=map(int,input().split())
def D(x,y):
    if y==1:return x%c
    t=D(x,y//2)**2
    if y%2:return t*x%c
    else:return t%c
print(D(a,b))

# 접근 제한시간 0.5초를 보면 단순 반복문 X, divide and conquer 필요
# 10^11 -> 10^5 * 10^5 * 10
# 10^5  -> 10^2 * 10^2 * 10
# 10^2  -> 10   * 10
