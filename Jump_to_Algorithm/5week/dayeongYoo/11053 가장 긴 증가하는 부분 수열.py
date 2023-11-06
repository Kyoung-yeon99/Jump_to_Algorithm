n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열

cache = [-1] * n


def lis(i):
    if cache[i] != -1:
        return cache[i]

    ans = 1
    for nxt in range(i + 1, n):
        if arr[i] < arr[nxt]:
            ans = max(ans, lis(nxt) + 1)
    cache[i] = ans
    return ans


max_length = 0  # Variable to store the maximum LIS length

for i in range(n):
    max_length = max(max_length, lis(i))

print(max_length)
