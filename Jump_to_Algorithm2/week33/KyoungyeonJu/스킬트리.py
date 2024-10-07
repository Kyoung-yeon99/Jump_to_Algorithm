def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        s = list(skill)
        is_right = True

        for i in tree:
            if i in skill:
                a = s.pop(0)
                if a != i:
                    is_right = False
                    break

        if is_right:
            answer += 1

    return answer