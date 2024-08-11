# 콜라츠 추측
# 1.짝수 -> 2로 나눔
# 2.홀수 -> 3을 곱하고, 1을 더함
# 3.결과로 나온 수가 1보다 크다면 1번 작업 반복

# 우박수열
# 콜라츠 추측으로 나온 수열을 우박수열
# 5-> 16 -> 8 -> 4 -> 2 -> 1

# 우박수열 꺾은선 그래프
# (0,5), (1,16), (2,8) ...

# x축 특정 구간 [a,b]에 대해 정적분 구하기
# 정적분: 그래프와 x축으로 둘러싸인 공간의 면적

# a,b: 각각 x축 시작점, 끝점 의미
# *b가 음수일 경우 -> 우박수열의 마지막에서부터 b만큼의 값 선택
# 예를 들어, [0, -1] -> 그래프 시작점(0)부터 끝점 바로 전(-1)까지 구간
# *[a,b]에서 a가 b보다 큰 경우 -> 정적분 결과: -1

# 주어진 우박수열 초항: k, 여러 구간 ranges에 대해 각각의 구간에 대한 정적분 결과 반환

def solution(k, ranges):
    answer = []  # 범위 내 정적분 결과
    seq = [k]  # 초항

    # 1. 우박수열 구하기
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        seq.append(k)

    # 2. 꺾은선 그래프-정적분: 삼각형+직사각형 면적 (x1, y1), (x2, y2)
    # 삼각형: abs(y1-y2)*0.5 -> x는 연속된 좌표로 위치함, 따라서 (x2-x1=1이라서 생략 가능)
    # 직사각형: min(y1, y2) -> x는 연속된 좌표로 위치함, 따라서 (x2-x1=1이라서 생략 가능)
    # 범위 내 면적 구하기
    areas = []
    for i in range(len(seq) - 1):
        y1 = seq[i]
        y2 = seq[i + 1]
        area = abs(y1 - y2) * 0.5 + min(y1, y2)
        areas.append(area)

    n = len(areas)
    for a, b in ranges:
        end = n + b  # 음수처리

        if a > end:
            answer.append(-1.0)
        else:
            answer.append(sum(areas[a:end]))

    return answer
