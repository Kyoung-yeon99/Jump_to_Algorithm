# 정확하게 N 킬로그램 배달
# 3, 5 kg 봉지 있을 때 가장 적은 봉지로 n 만들기 (못만들면 -1)

n = int(input())

cnt = n // 5

for i in range(0, n//5 + 1):
    temp = ((n % 5) + (5 * i))
    if temp % 3 == 0:
        cnt += (temp // 3)
        break
    else:
        cnt -= 1

print(cnt)