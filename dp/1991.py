# https://www.acmicpc.net/problem/1991
# 트리 순회
# 재귀
t={}
for l in [*open(0)][1:]:s,*c=l.split();t[s]=[x if x!='.'else''for x in c]
a=b=c=''
def R(s):
    global a,b,c;l,r=t[s];a+=s
    if l:R(l)
    b+=s
    if r:R(r)
    c+=s
R('A')
print(a,b,c,sep='\n')
# tip: sep='\n' 대신 사용할 수 있는 방법 *map(print,r)
