def solution(targets):
    answer = 0
    # 개구간 (s, e)로 표현되는 폭격 미사일은 s와 e에서 발사하는 요격 미사일로는 요격할 수 없음
    # 요격 미사일은 실수인 x 좌표에서도 발사 가능
    # 모든 폭격 미사일을 요격하기 위해 필요한 최소 요격 미사일 수
    # 이분탐색 범위
    targets = sorted(targets, key=lambda x: x[1])
    cur = 0
    # 모든 폭격 미사일을 요격하기 위해 길이가 작은 미사일 먼저 폭격
    for i in range(len(targets)):
        if cur > targets[i][0]:
            continue
        else:
            cur = targets[i][1]
            answer += 1

    return answer



tcs = [
    [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
]

for tc in tcs:
    solution(tc)
