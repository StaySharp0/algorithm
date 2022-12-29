# https://www.acmicpc.net/problem/1918
# 후위 표기식
# stack
s=[]
r=''
p={'(':0,'+':1,'-':1,'*':2,'/':2} 
for c in input():
    print(s)
    if c.isalpha():r+=c
    elif c=='(':s.append(c)
    elif c==')':
        while s and s[-1]!='(':r+=s.pop()
        s.pop()
    else:
        while s and p[c]<=p[s[-1]]:r+=s.pop()
        s.append(c)
while s:r+=s.pop()
print(r)

# 알파벳인 경우 출력
# 우선 순위가 높은 연산자가 먼저 나온다(후입선출)
# ( ) 구간이 끝나면 먼저 출력 
# 쌓여있는 연산자 중에 자신과 같거나 높은 우선순위들은 출력
