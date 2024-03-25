import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
info = list(map(int, input().split()))
watch_out_number = info[0]
if watch_out_number > 0: # 이야기의 진실을 아는 사람이 있을 경우
    watch_out = info[1:]
    party = []
    connected = [[] for _ in range(N+1)] # 인접 리스트(같은 파티에 참석하는 사람들)
    checked = [False for _ in range(N+1)]
    count = 0

    for i in range(M):
        participants = list(map(int, input().split()))
        if participants[0] > 0:
            for p in participants[1:]:
                connected[p].extend(participants[1:])
                connected[p] = list(set(connected[p])) # 중복 제거
            party.append(participants)

    q = deque(watch_out)
    for p in watch_out:
        checked[p] = True

    while q: # 진실을 아는 사람과 연결된 사람 확인
        next = q.popleft()
        for p in connected[next]:
            if not checked[p]:
                checked[p] = True
                q.append(p)
                watch_out.append(p)

    for i in range(M): # 각 파티가 거짓말을 해도 되는 사람들로 구성되어 있는지 확인
        tell_truth = False
        for j in range(1, party[i][0]+1):
            if party[i][j] in watch_out:
                tell_truth = True
                break
        if not tell_truth:
            count += 1
    print(count)

else: # 이야기의 진실을 아는 사람이 없을 경우
    print(M) # 모든 파티에서 과장된 이야기를 할 수 있음


        
