def solution(keymap, targets):
    hash = {}  # 각 문자의 최소 클릭 횟수 등록
    ans = []

    for key in keymap:
        btn = 0  # 버튼 클릭 횟수
        for k in key:
            btn += 1
            if k not in hash:
                hash[k] = btn
            else:
                hash[k] = min(hash[k], btn)

    for target in targets:
        click = 0  # 총 클릭 횟수
        for t in target:
            if t not in hash:  # 만들 수 없는 문자열
                click = -1
                break

            else:
                click += hash[t]

        ans.append(click)

    return ans