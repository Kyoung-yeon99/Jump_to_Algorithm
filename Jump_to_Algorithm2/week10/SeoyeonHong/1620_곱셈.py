# A를 B번 곱한 수를 C로 나눈 나머지

# 지수법칙
# b가 짝수: a^b = a^(b/2+b/2) = a^(b/2) * a^(b/2)
# b가 홀수: a^b = a^(b/2 + b/2+1) = a^(b/2) * a^(b/2+1)

# 나머지 연산의 성질
# (a * b) % c = (a % c * b % c) % c

A, B, C = map(int, input().split()) 

def calculate(a, b, c):
    if b == 1:
        return a % c
    k = calculate(a, b // 2, c)
    if b % 2 == 0: # b가 짝수라면    
        return (k * k) % c
    else:
        return (k * k * a) % c

print(calculate(A, B, C))