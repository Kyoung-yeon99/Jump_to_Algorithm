T = int(input())
d = [1, 2, 4] + [0] * 7  # 1 <= n < 11
nums = [int(input()) for _ in range(T)]

# 1, 2, 3만 더하기 가능!
# d[i-1] 값에 1 더하기 + d[i-2] 값에 2 더하기 + d[i-3] 값에 3 더하기
for i in range(3, 10):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for num in nums:
    print(d[num-1])
