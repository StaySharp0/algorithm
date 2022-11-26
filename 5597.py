# https://www.acmicpc.net/problem/5597
R=[0]*31
for i in open(0):i=int(i);R[i]=i
for i,x in enumerate(R):
    if i!=0 and x==0: print(i)
