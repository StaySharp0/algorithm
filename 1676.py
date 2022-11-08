#  # https://www.acmicpc.net/problem/1676
N=int(input())
i,R=1,[]
while i*5<=N:
    a,x=0,i*5
    while x%5==0:
        x//=5
        a+=1
    R.append(a)
    i+=1
print(sum(R))

# 5*2가 몇개 나오는지 계산하는 문제
# 2는 충분히 나오므로 5의 갯수만 세면됨 
