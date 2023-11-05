def combination(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else: # 4 이상일 경우 (n-1) + 1, (n-2) + 2, (n-3) + 3으로 표현 가능
        return (combination(n-1) + combination(n-2) + combination(n-3))

t = int(input())
for _ in range(t):
    n = int(input())
    print(combination(n))

