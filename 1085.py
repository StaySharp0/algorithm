print(min((s:=[*map(int, input().split())])[0], s[1], s[3]-s[1], s[2]-s[0]))

# x,y,w,h=map(int,input().split())
# print(min(x,y,h-y,w-x))
# 계산할 데이터가 정해져있으면 굳이 리스트로 처리 안해도됨