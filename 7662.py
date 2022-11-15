# https://www.acmicpc.net/problem/7662
# 우선순위 큐 

# 메모리 초과, open()이 문제인듯heapq
#from heapq import*
#P=heappop
#H=heappush
#I=[]
#A=[]
#for s in[s.split()for s in[*open(0)][2:]]:
#    c=s[0]
#    if len(s)==2:n=int(s[1])
#    elif I==[]:print('EMPTY')
#    else:print(P(A)[1],P(I))
#    if c=='I':H(I,n);H(A,[-n,n])
#    elif I==[]:continue
#    elif n==1:I.remove(P(A)[1])
#    elif n==-1:
#        C=P(I)
#        for i in A:
#            if i[1]==C:A.remove(i)
#print(P(A)[1],P(I))

# 시간초과, remove 제거, 방문정보로 동기화
import sys,heapq
R=sys.stdin.readline
P=heapq.heappop
H=heapq.heappush
G=range
N=int
for _ in G(N(R())):
    I=[];A=[];V={}
    for s in G(N(R())):
        s=R().split()
        n=N(s[1])
        if s[0]=='I':H(I,n);H(A,-n);V.setdefault(n,0);V[n]+=1
        else:
            T=A if n==1 else I
            while T!=[]:
                t=P(T)*(-1 if n==1 else 1)
                if V[t]:V[t]-=1;break
    V=[k for k,v in V.items()if v>0];V.sort()
    print('EMPTY'if V==[]else'%d %d'%(V[-1],V[0]))
