# https://www.acmicpc.net/problem/14681
M='-'
T=True
F=False
O={T:{T:3,F:2},F:{F:1,T:4}}
I=input
print(O[I()[0]==M][I()[0]==M])
