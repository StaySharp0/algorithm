input()
c = -1
print(sum([(ord(w)-96)*(31**(c:= c+1)) for w in input()]) % 1234567891)