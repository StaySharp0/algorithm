# https://www.acmicpc.net/problem/1764
S='\n'
I=[*open(0)]
N=int(I[0].split()[0])
O={}
R=[]
for i,s in enumerate(I[1:]):
    if i<N:O[s]=1
    elif s in O:R.append(s[:-1])
R.sort()
print(len(R),S.join(R),sep=S)

# set 교집합을 활용하는 방법이 있음
# n,m=map(int,input().split())
# d={input()for _ in range(n)}
# b={input()for _ in range(m)}
# print(len(d&b),*sorted(d&b))
