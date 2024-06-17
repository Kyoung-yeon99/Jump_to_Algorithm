# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    count = 0
    idx = 0 # section 중 칠하지 않은 영역의 가장 장은 인덱스
    while idx < len(section):
        start = section[idx] # 칠할 범위의 시작
        end = min(n+1, start+m) # 칠할 범위의 끝
        for num in range(start, end):
            if num == section[idx]: # 칠하지 않은 부분이라면
                idx += 1 # 인덱스 값 +1
                if idx == len(section): # 다 칠했다면 종료
                    break
        count += 1 # 칠한 횟수 +1
    return count