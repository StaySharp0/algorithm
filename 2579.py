# https://www.acmicpc.net/problem/2579
# DP
I=[int(n)for n in open(0)]
N=I[0]
I=I[1:]+[0]*300
V=[I[0],I[1]+I[0],max(I[2]+I[1],I[2]+I[0])]
for i in range(3,N):V.append(I[i]+max(V[i-2],I[i-1]+V[i-3]))
print(V[N-1])

# 구하고자 하는 계단의 경우의 수는 2개
# 1. 계단 값:I(n) + 1칸 전 계단:I(n-1) + 3칸 전 계단 합:V(n-3)
# 2. 계단 값:I(n) + 2칸 전 계단 합:V(n-2) 


# x,b,d=int(input()),0,[0]*305
# for i in range(3,x+3):
#     b,d[i]=(n:=int(input())),max(d[i-3]+b,d[i-2])+n
# print(d[x+2])
