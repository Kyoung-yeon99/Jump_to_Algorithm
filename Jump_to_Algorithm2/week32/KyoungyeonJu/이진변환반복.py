def solution(s):
    cnt, zero = 0, 0  # 이진 변환 회수, 제거된 0의 개수
    s = list(s)

    while s != ["1"]:  # 문자열 s가 1이 될 때까지 반복
        zero_cnt = s.count("0")
        zero += zero_cnt  # 제거될 0의 개수 합산
        cnt += 1  # 이진 변환 횟수 1 증가

        s = ["1"]*(len(s) - zero_cnt)
        s = list(bin(len(s))[2:])

    return [cnt, zero]


"""
# 시간 초과
        if zero_cnt != 0:
            # remove 메서드는 하나의 요소만 삭제
            [s.remove("0") for _ in range(zero_cnt)] 
"""
