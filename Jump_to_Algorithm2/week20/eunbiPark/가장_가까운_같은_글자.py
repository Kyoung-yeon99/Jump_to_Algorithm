def solution(s):
    hash = {}  # 마지막 등장 idx 등록
    ans = []

    for idx, char in enumerate(s):
        if char not in hash:
            ans.append(-1)
        else:
            ans.append(idx - hash[char])

        hash[char] = idx

    return ans