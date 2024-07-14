# 투포인터 풀이
def solution(sequence, k):
    l = len(sequence)
    s = 0  # 연속된 부분 수열의 합
    end = 0   # 연속된 부분 수열의 마지막 인덱스
    a = []  # 조건을 만족하는 부분 수열의 시작 인덱스, 마지막 인덱스, 길이

    for i in range(l):
        while s < k and end < l:
            s += sequence[end]
            end += 1

        if s == k:
            a.append([i, end-1, end-1-i])

        s -= sequence[i]  # 합이 k와 같거나 초과

    a = sorted(a, key=lambda x: x[2])  # 길이를 기준으로 정렬
    return a[0][:2]


"""
# 누적합 + lower bound 
 def solution(sequence, k):
    L = len(sequence)
    sequence = [0] + sequence

    for i in range(1, L+1):
        sequence[i] = sequence[i-1] + sequence[i]

    for l in range(1, L + 1):
        if sequence[-1] - sequence[-1 - l] < k:
            continue
        if sequence[l] - sequence[0] > k:
            break

        s = 0
        e = L - l

        while s < e:
            m = (s + e) // 2
            if sequence[m+l] - sequence[m] >= k:
                e = m
            else:
                s = m + 1

        if sequence[s+l] - sequence[s] == k:
            return [s, s + l - 1]
"""


