def solution(n, l, r):
    def cnt(idx):
        # 좀 더 빠른 코드
        while idx > 0:
            if idx % 5 == 2:
                return 0
            idx //= 5
        return 1

        # if idx % 5 == 2:  # 중앙의 값이라면
        #     return 0
        # elif idx < 5:  # 1번째 유사 칸토어 비트열
        #     return 1
        # return cnt(idx//5)

    answer = 0
    for i in range(l-1, r):
        answer += cnt(i)

    return answer


"""
# 시간초과
def solution(n, l, r):
    a = '11011'
    b = '00000'
    c = a+a+b+a+a
    arr = [1, a, c]

    for i in range(3, n+1):
        before = arr[i-1]
        i, new = 0, ''
        while len(before) > i:
            five = before[i:i+5]
            if five == a:
                new += c
            elif five == b:
                new += b*5
            i += 5
        arr.append(new)
        
    num = arr[n][l-1:r]
    answer = sum(map(int, num))
    
    return answer
"""