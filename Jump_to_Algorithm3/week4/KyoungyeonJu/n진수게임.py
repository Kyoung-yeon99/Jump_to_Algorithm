def solution(n, t, m, p):
    # 진법 n, 미리 구할 숫자의 개수 t, 게임 참가 인원 m, 튜브 순서 p
    def transform(x, n):  # 10진수 x값을 n진수로 변환
        def check(xx):  # 대문자로 나타낼 값인지 확인
            a = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            if xx in a.keys():
                return a[xx]
            return str(xx)

        y = ''
        while x > n-1:
            y += check(x % n)
            x = x // n

        y += check(x)
        return y[::-1]

    num, nums = 2, '01'

    while len(nums) < t * m:
        nums += transform(num, n)
        num += 1

    answer = ''
    for i in range(t):
        answer += nums[i*m+p-1]

    return answer