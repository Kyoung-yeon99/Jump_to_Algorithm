from itertools import combinations

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])

    # 가능한 모든 컬럼 조합
    all_combinations = []
    for i in range(1, col_len + 1):
        all_combinations.extend(combinations(range(col_len), i))
    candidate_keys = []

    # 각 조합별로 유일성이랑 최소성 확인
    for comb in all_combinations:
        # 유일성
        unique_rows = set(tuple(relation[row][col] for col in comb) for row in range(row_len))

        # 유일성을 만족하는 경우
        if len(unique_rows) == row_len:
            # 최소성 확인
            is_minimal = True
            for key in candidate_keys:
                if set(key).issubset(comb):
                    is_minimal = False
                    break
            # 최소성을 만족하면 후보키로 추가하기
            if is_minimal:
                candidate_keys.append(comb)

    return len(candidate_keys)


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(relation))