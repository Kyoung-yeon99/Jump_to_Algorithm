def solution(n, left, right):
    answer = []
    first = [1,2,3, 2,2,3, 3,3,3]
    second = [1,2,3,4, 2,2,3,4, 3,3,3,4, 4,4,4,4]
    for i in range(left, right +1):
        r = i // n
        c = i % n
        print(r, c)
        ans = -1
        if r == 0:
            ans = c+1
        elif r == n-1:
            ans = n
        else:
            if c <= r-1:
                ans = r+1
            else:
                ans = c+1
        answer.append(ans)
    return answer


"""
3	2	5	[3,2,2,3]
4	7	14	[4,3,3,3,4,4,4,4]
"""

tcs = [
    [3,	2,	5],
    [4,	7,	14]
]

for tc in tcs:
    print(solution(*tc))
    print()
