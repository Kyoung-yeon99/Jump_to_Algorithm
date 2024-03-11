from collections import defaultdict


def calculate(aa, num):
    matrix = []
    max_len = 0
    for i in range(len(aa)):
        dic = defaultdict(int)
        q = []
        for j in range(len(aa[i])):
            if aa[i][j] != 0:
                dic[aa[i][j]] += 1
        for key, value in dic.items():
            q.append([key, value])  # 개수, 숫자
        q.sort(key=lambda x: [x[1], x[0]])  # 개수 기준으로 정렬하기
        qq = sum(q, [])  # 이어붙이기
        max_len = max(max_len, len(qq))  # 가장 긴 길이 구하기
        matrix.append(qq)

    for i in matrix:
        i += [0]*(max_len-len(i))  # 0 추가
        if len(i) > 100:
            i = i[:100]

    return matrix if num == 1 else list(zip(*matrix))


r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
while True:
    if cnt > 100:
        cnt = -1
        break
    if r-1 < len(a) and c-1 < len(a[0]):
        if a[r-1][c-1] == k:
            break
    if len(a) >= len(a[0]):  # 행의 개수 >= 열의 개수 -> R 연산
        a = calculate(a, 1)
    else:  # C 연산
        a = calculate(list(zip(*a)), 2)
    cnt += 1

print(cnt)
