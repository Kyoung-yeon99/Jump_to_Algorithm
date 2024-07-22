n = int(input())
times = list(map(int, input().split()))
times.sort()
lens = len(times)
ans = 0

for i in range(len(times)):
    ans += times[i]*(lens-i)

print(ans)