# N, M은 50 이하의 자연수 각각 사람의 수, 파티의 수
# 진실을 아는 사람의 수는 0 이상 50 이하의 정수
# 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수
# 지민이는 모든 파티에 참가해야한다.
# 지민이는 이야기를 과장되게 한다. 또한 지민이는 거짓말쟁이가 되기 싫다.
# 이야기의 진실을 아는 사람이 파티에 있으면 과장해서 말할 수 없다.
# 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 문제.
# 자료구조의 활용을 요구하는 유형의 문제
# https://dreamtreeits.tistory.com/32

from sys import stdin

n, m = map(int, stdin.readline().split())
trues = set(list(map(int, stdin.readline().split()))[1:])
party = []
cnt = []

for _ in range(m):
    data = set(map(int, stdin.readline().split()[1:]))
    if data:
        party.append(data)
        cnt.append(1)

for _ in range(m):
    for i, p in enumerate(party):
        if trues & p:
            cnt[i] = 0
            trues |= p
