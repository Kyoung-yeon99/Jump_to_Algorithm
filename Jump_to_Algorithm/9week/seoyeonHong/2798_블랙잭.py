# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합
n, m = map(int, input().split()) # 카드의 개수, 최댓값
a = list(map(int, input().split())) # 카드에 쓰여 있는 수
a.sort() # 오름차순 정렬
max_sum = 0 # 합의 최댓값

for i in range(n-2):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = a[i] + a[j] + a[k]
            print(i, j, k)
            if sum > max_sum and sum <= m:
                max_sum = sum

print(max_sum)
