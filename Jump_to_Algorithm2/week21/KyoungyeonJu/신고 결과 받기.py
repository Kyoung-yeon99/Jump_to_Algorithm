def solution(id_list, report, k):
    d = {}  # user 이름과 index 딕셔너리
    l = len(id_list)
    m = [[0] * l for _ in range(l)]  # 신고 유저ID와 신고된 유저ID를 모두 저장할 인접 행렬
    reported = []  # 정지된 유저
    answer = []

    for i, user in enumerate(id_list):
        d[user] = i

    for r in report:
        a, b = r.split()
        a, b = d[a], d[b]
        m[a][b] = 1  # 여러번 신고해도 횟수는 1회로 처리

    nm = list(map(list, zip(*m)))  # 정지된 유저를 구하기 위해 전치행렬

    for i, row in enumerate(nm):
        if sum(row) >= k:
            reported.append(i)

    if not reported:  # 정지된 유저가 없는 경우 바로 return
        return [0] * l

    for row in m:
        if sum(row) == 0:  # 신고한 유저가 없는 경우 정지된 유저도 없으므로 0 append
            answer.append(0)
        else:
            num = 0
            for i in reported:
                if row[i] == 1:
                    num += 1
            answer.append(num)

    return answer