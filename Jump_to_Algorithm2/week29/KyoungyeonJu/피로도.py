import itertools

def solution(k, dungeons):
    answer = 0
    d_num, d_len = [i for i in range(len(dungeons))], len(dungeons)

    d = itertools.permutations(d_num, d_len)
    for row in d:
        ans, kk = 0, k
        for i in row:
            need, consume = dungeons[i][0], dungeons[i][1]
            if kk >= need:
                kk -= consume
                ans += 1
            else:
                break
        answer = max(answer, ans)

    return answer


"""
80	[[80,20],[50,40],[30,10]] 3
"""

tcs = [
    [80, [[80,20],[50,40],[30,10]]]
]

for tc in tcs:
    print(solution(*tc))
