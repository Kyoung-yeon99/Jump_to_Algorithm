def solution(keymap, targets):
    keys = dict()
    answer = []

    for kk in keymap:
        l = list(kk)
        for idx, key in enumerate(l):
            if key not in keys:
                keys[key] = idx+1
            else:
                if idx < keys[key]:
                    keys[key] = idx + 1

    for target in targets:
        ans = 0
        t = list(target)
        for i in t:
            if i in keys.keys():
                ans += keys[i]
            else:
                ans = -1
                break

        answer.append(ans)

    return answer


