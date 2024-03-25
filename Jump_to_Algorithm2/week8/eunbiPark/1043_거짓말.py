import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 사람 수, 파티 수
knows = set(input().split()[1:]) # 진실을 아는 사람 수, 번호 (1 ~ n)
# knows = set(map(int, input().split()[1:])) # 진실을 아는 사람 수, 번호 (1 ~ n)
# print(knows)
# 파티에 참여한 사람과 비밀을 아는 사람의 교집합이 있다면
# 그 사람으로 인해 모두가 진실을 알게 된다
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for p in parties:
        if p & knows:
            knows = knows.union(p)

cnt = 0
for p in parties:
    if p & knows:
        continue
    cnt += 1

print(cnt)