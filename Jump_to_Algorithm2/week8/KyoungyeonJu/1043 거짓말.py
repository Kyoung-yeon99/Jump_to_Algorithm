import sys
input = sys.stdin.readline
# 0 <= 사람, 파티 <= 50, 1 <= 파티에 오는 수 <= 50
n, m = map(int, input().split())
true = list(map(int, input().split()))
true_num = set(true[1:])  # 진실을 아는 사람 번호
parties = []
ans = [False]*m

for _ in range(m):
    p = list(map(int, input().split()))
    parties.append(set(p[1:]))  # & 연산을 위해 같은 데이터형 sets

if true[0] != 0:  # 진실을 아는 사람이 있는 경우
    for _ in range(m):
        for party in parties:
            if party & true_num:  # 교집합이 있다면
                true_num = true_num.union(party)  # true_num은 합집합

print("진실을 아는 사람들", true_num)
for i in range(m):
    if true_num & parties[i]:
        ans[i] = True

print(ans.count(False))

