# https://school.programmers.co.kr/learn/courses/30/lessons/147354

# 테이블의 해시 값
def solution(data, col, row_begin, row_end):
    answer = 0
    # col번째 컬럼의 값을 기준으로 오름차순 정렬, 첫 번째 컬럼의 값을 기준으로 내림차순 정렬
    data.sort(key = lambda x: (x[col-1], -x[0]))
    S = []
    for i in range(row_begin-1, row_end):
        s = 0
        # i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합
        for element in data[i]:
            s += element % (i+1)
        S.append(s)
    
    # S_i를 누적하여 bitwise XOR
    for s in S:
        answer ^= s
    
    return answer