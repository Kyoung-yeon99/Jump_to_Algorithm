# 랭킹 리스트에 올라 갈 수 있는 점수 개수 p  10 <= p <= 50
# 이미 랭킹 리스트에 있는 점수 개수 n   0 <= n <= p

n, new, p = map(int, input().split())
if n == 0:
    print(1)
    exit()
else:
    nums = list(map(int, input().split()))

nums.append(new)
nums.sort(reverse=True)

for i in range(len(nums)-1, -1, -1):
    if nums[i] == new and i > p - 1:
        print(-1)
        exit()

print(nums.index(new)+1)


