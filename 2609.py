A,B = map(int, input().split())
A,B = (A,B) if A > B else (B,A)
X,Y = A,B

while (T:=X % Y) != 0:
  X=Y
  Y=T

print(Y)
print(A*B//Y)

# 최대공약수 gcd = 유클리도 호제법
# 최소공배수 lcm = 두 자연수의 곱 / 최대공약수