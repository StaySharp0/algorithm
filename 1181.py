# https://www.acmicpc.net/problem/1181
# 정렬 문자열
# 배열 문자열 출력

W=[*set([*open(0)][1:])]
W.sort()
W.sort(key=lambda w:len(w))
print(*W,sep="")