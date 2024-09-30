def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    rot = [[1, 0], [0, 1], [-1, -1]]  # 반시계 방향으로 채우기: r+1 증가, c+1 증가, r-1감소와 c-1감소 반복
    num, r, c = 1, -1, 0
    rot_num = 0

    for i in range(n, 0, -1):
        rr, cc = rot[rot_num % 3]
        for j in range(i):
            nr, nc = r + rr, c + cc
            answer[nr][nc] = num
            r, c = nr, nc
            num += 1
        rot_num += 1

        # 2차원 리스트 -> 1차원 리스트
        real_answer = []
        while len(answer):
            list = answer.pop(0)
            real_answer.extend(list)

        return real_answer


"""
# 2차원 리스트 -> 1차원 리스트
1. pop하고 extend
테스트 7 〉	통과 (120.87ms, 43MB)
테스트 8 〉	통과 (107.37ms, 43.2MB)
테스트 9 〉	통과 (105.76ms, 43.3MB)

2. itertools.chain(*list)
테스트 7 〉	통과 (154.51ms, 43.1MB)
테스트 8 〉	통과 (142.49ms, 43.2MB)
테스트 9 〉	통과 (151.86ms, 43.2MB)

3. sum(answer, [])
테스트 7 〉	통과 (1723.80ms, 45.3MB)
테스트 8 〉	통과 (1806.23ms, 45.2MB)
테스트 9 〉	통과 (1695.21ms, 45.2MB)
"""