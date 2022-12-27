# https://www.acmicpc.net/problem/1526
# 가장 큰 금민수
# brute-force
for i in range(int(input()),3,-1):
    if all([c=='4'or c=='7'for c in str(i)]):print(i);break

# tip: all, any 내장함수
