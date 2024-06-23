def solution(today, terms, privacies):
    # 날짜로 변환
    def time_conv(t):
        year, month, day = map(int, t.split('.'))
        return year * 12 * 28 + month * 28 + day

    hash = {}
    today = time_conv(today)
    ans = []

    # hash 등록
    for t in terms:
        name, period = t.split()
        hash[name] = int(period) * 28

    # 각 날짜 변환
    for idx, privacy in enumerate(privacies):
        start, name = privacy.split()
        end = time_conv(start) + hash[name]

        if end <= today:
            ans.append(idx + 1)

    return ans

'''
# 틀린 풀이
def solution(today, terms, privacies):
    ans = []

    # 0. terms -> hash
    hash = {}
    for t in terms:
        category, m = t[0], int(t[2:])
        hash[category] = m

    # 1. 유효기간 구하기
    for idx, p in enumerate(privacies):
        category = p[-1]
        year = int(p[:4])
        month = int(p[5:7])
        day = int(p[8:-1])

        month += hash[category]
        day -= 1
        if day <= 0:
            day = 28
            month -= 1

        if month > 12:
            year += (month // 12)
            month %= 12

        # 2. 유효한지 확인하기
        if year < int(today[:4]):
            ans.append(idx + 1)
        elif month < int(today[5:7]):
            ans.append(idx + 1)
        elif day < int(today[8:]):
            ans.append(idx + 1)

    return ans
'''