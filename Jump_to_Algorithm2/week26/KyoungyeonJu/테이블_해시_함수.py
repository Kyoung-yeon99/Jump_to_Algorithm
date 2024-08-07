def solution(data, col, row_begin, row_end):
    # 테이블을 col번째 컬럼의 값 기준 오름차순, 만약 그 값이 동일하면 첫 번째 컬럼 값 기준으로 내림차순 정렬
    # row_begin ≤ i ≤ row_end
    # S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의
    # 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환

    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    answer = 0
    for i in data[row_begin-1]:
        answer += i % row_begin

    for i in range(row_begin+1, row_end+1):
        mod = 0
        for j in data[i-1]:
            mod += j % i
        answer ^= mod

    return answer