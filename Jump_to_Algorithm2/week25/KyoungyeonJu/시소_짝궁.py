# 정렬과 Counter을 활용한 풀이
from collections import Counter


def solution(weights):
    answer = 0
    weights.sort()
    c = Counter(weights)  # 각 weight의 개수 계산
    # print(c)
    for i in range(len(weights) - 1):
        w = weights[i]
        c[w] -= 1
        # print(w, c[w])
        for j in [1, 3 / 2, 4 / 3, 2]:  # 정렬이 되어 있기 때문에 4가지의 경우의 수만 계산
            if w * j in c.keys():  # 해당 값의 존재 확인
                answer += c[w*j]
                #print(f'j={j} 곱한 값 = {w*j} answer = {answer} {c}')

    return answer



"""
[100,180,360,100,270]	4
[180,180,360,270]	6
[180, 180, 180]  3
"""

tcs = [
    [100, 180, 360, 100, 270],
    [180, 180, 360, 270],
    [180, 180, 180]
]

for tc in tcs:
    print(solution(tc))
    print()

"""
# 시간초과 35.3 / 100.0
def solution(weights):
    answer = 0
    weights.sort()
    for i in range(len(weights)-1):
        nw = weights[i+1:]
        w = weights[i]
        for j in [1, 3/2, 4/3, 2]:
            if w*j in nw:
                answer += nw.count(w*j)
    return answer
"""


"""
# defaultdict 활용 풀이
from collections import defaultdict


def solution(weights):
    # 2 ≤ len(weights) ≤ 100,000      100 ≤ weights[i] ≤ 1,000
    ans = 0
    info = defaultdict(int)
    for w in weights:
        ans += info[w] + info[w * 2] + info[w / 2] + info[(w * 2) / 3] + info[(w * 3) / 2] + info[(w * 3) / 4] + info[
            (w * 4) / 3]
        info[w] += 1

    return ans

"""