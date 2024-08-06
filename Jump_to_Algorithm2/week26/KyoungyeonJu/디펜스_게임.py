import heapq


def solution(n, l, r):
    # 0번째 유사 칸토어 비트열은 1
    # n 번째 유사 칸토어 비트열은 n-1번재 유사 칸토어 비트열에서의 1을 11011로 치환, 0을 00000로 치환
    # n 번째 유사 칸토어 비트열에서 특정 구간 내의 1의 개수

    answer = 0
    return answer
def solution(n, k, enemy):
    # 남은 병사 중 enemy[i] 명 만큼 소모해서 enemy[i] 적 막을 수 있음
    # 남은 병사의 수보다 현재 라운드의 적의 수가 더 많으면 게임 종료
    # 무적권 스킬을 사용하면 병사의 소모없이 한 라운드의 공격을 막을 수 있음, 최대 k번 사용 가능
    # 최대 몇 라운드까지 막을 수 있는지 return, 모든 라운드를 막을 수 있는 경우 enemy 길이 return

    l = len(enemy)
    if l <= k:  # enemy 길이가 k 이하인 경우
        return l

    h = []
    # 먼저 k개의 enemy 값을 heapq에 넣기
    for i in range(k):
        heapq.heappush(h, enemy[i])

    # enemy[i] 값 push, pop한 값을 n에서 빼기,
    for i in range(k, l):
        heapq.heappush(h, enemy[i])
        num = heapq.heappop(h)
        if num > n:
            return i
        n -= num

    # 모든 라운드를 막으면 enemy 길이 return
    return l


"""
7	3	[4, 2, 4, 5, 3, 3, 1]	5
2	4	[3, 3, 3, 3]	4
"""

tcs = [
    [7,	3,	[4, 2, 4, 5, 3, 3, 1]],
    [2,	4,	[3, 3, 3, 3]]
]

for tc in tcs:
    print(solution(*tc))
    print()