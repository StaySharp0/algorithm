H, M = map(int, input().split(' '))
print((24 + H - 1) % 24 if M < 45 else H, (60 + M - 45) % 60)

# a,b=map(int,input().split())
# print((a-(b<45))%24,(b-45)%60)
# ' ' 안해도 되네
# True는 1로 False는 0 으로 묵시적 치환됨 / % 연산 수행시 minus 저절로 처리됨