def power(a, b):
    if b == 1:
        return a % C
    else:
        temp = power(a, b // 2)  # a^(b // 2)
        if b % 2 == 0:  # 지수가 짝수인 경우
            return temp * temp % C
        else:  # 홀수인 경우
            return temp * temp * a % C


A, B, C = map(int, input().split())
print(power(A, B))
