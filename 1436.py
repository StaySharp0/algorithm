# https://www.acmicpc.net/problem/1436
# 브루트포스
# 10.000 수를 666 숫자 앞뒤로 붙이고 정렬해서 해당 찾고자하는 순위 출력 - X
# 1부터 원하는 순위의 숫자가 나오면 출력후 종료

N=int(input())-1
S=666
while N != 0:
  S+=1
  if '666' in str(S):
    N-=1
print(S)