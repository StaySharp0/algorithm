# https://www.acmicpc.net/problem/10807
T=int
I=[*open(0)]
R=0
for i in I[1].split():
    if T(i)==T(I[2]):R+=1
print(R)
