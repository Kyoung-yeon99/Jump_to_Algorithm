def func(start):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    for i in range(start, n+1):
        if i not in result:
            result.append(i)
            func(i+1)  # 오름차순 수열을 위해 i+1
            result.pop()


# 1 ≤ M ≤ N ≤ 8
n, m = map(int, input().split())
result = []
func(1)
