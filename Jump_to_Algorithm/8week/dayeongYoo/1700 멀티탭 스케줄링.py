from collections import deque

N, K = map(int, input().split())
q = list(map(int, input().split()))

INF = float('inf')


def off_least_plug():
    global N, K, q

    cnt = 0
    on_plug = set()
    rest = dict()

    # 각 제품의 task list 구하기
    for i, task in enumerate(q):
        if task in rest:
            rest[task].append(i)
        else:
            rest[task] = deque([i])

    # 추후 정렬을 위해 task 없는 제품에는 무한대 저장
    for i in range(1, K + 1):
        if i not in rest:
            rest[i] = deque([INF])

    for idx, now_task in enumerate(q):
        # 이번 차례 제품이 콘센트에 꼽혀있지 않을 때
        if now_task not in on_plug:
            # 콘센트 자리 남아있는 경우
            if len(on_plug) < N:
                on_plug.add(now_task)
            # 콘센트 자리 없는 경우
            else:
                # 콘센트에 꼽혀있는 제품들의 남은 task list 불러와서
                # 가장 나중에 사용하는 (또는 사용이 끝난) 제품 찾기
                temp_dict = {key: value for key, value in rest.items() if key in on_plug}
                rank = sorted(temp_dict.items(), key=lambda x: x[1][0], reverse=True)
                deleted = rank[0][0]
                on_plug.remove(deleted)
                on_plug.add(now_task)
                cnt += 1

        # 이번 차례 제품의 rest list 갱신
        # 사용 끝났으면 무한대 넣어주기
        rest[now_task].popleft()
        if len(rest[now_task]) == 0:
            rest[now_task].append(INF)

    return cnt


print(off_least_plug())
