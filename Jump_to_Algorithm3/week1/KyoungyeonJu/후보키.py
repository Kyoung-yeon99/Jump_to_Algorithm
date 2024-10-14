from itertools import combinations

def solution(relation):
    answers, answer = [], []
    row, col = len(relation), len(relation[0])
    check = [i for i in range(col)]

    num = 1
    while num < col+1:
        for c in combinations(check, num):
            tmp = [tuple(row[i] for i in c) for row in relation]
            if len(set(tmp)) == row:
                answers.append(c)
        num += 1

    for tup in answers:
        is_minimal = True
        for other in answers:
            # set1.issuperset(set2), set1이 set2의 상위집합이면 True
            if tup != other and set(tup).issuperset(set(other)):
                is_minimal = False
                break
        if is_minimal:
            answer.append(tup)

    return len(answer)