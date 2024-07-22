def solution(s):
    answer = []
    d = {}  # 글자들의 최신 인덱스 Update

    for idx, ss in enumerate(s):
        if ss in d:
            answer.append(idx - d[ss])
        else:
            answer.append(-1)

        d[ss] = idx

    return answer