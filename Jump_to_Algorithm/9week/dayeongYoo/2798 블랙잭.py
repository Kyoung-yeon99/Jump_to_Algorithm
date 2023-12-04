# n장 중 3장 고름. 고른 카드의 합은 m과 가까우면서 m을 넘지않아야 함.

n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
for i in range(n):  # 1st
    for j in range(i + 1, n):  # 2nd
        for k in range(j + 1, n):  # 3rd
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                ans = max(ans, cards[i] + cards[j] + cards[k])

print(ans)