# https://www.acmicpc.net/problem/1107
# 브루트포스
N,*_,M=open(0)
if len(_)==0:M=''
N=int(N);R=abs(N-100);
for n in range(1000001):
    X=str(n)
    for x in X:
        if x in M:break 
    else:R=min(R,len(X)+abs(N-n)) 
print(R)

# +- 고려해서 abs, 100001
# 버튼 누르는 걸로 못찾는 경우 무시 / 눌러서 만들 수 있으면 차이+-계산 
# python tip: for...else for을 다 돌면 else 수행
