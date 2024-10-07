def solution(skill, skill_trees):
    answer = 0
    for cur_skill_tree in skill_trees:
        cur_skill_tree_id = 0
        stack = []
        possible = True

        #스킬 빼고 문자열 다 제거
        while cur_skill_tree_id < len(cur_skill_tree):
            if cur_skill_tree[cur_skill_tree_id] in skill: #스킬 트리 확인
                stack.append(cur_skill_tree[cur_skill_tree_id])
            cur_skill_tree_id+=1 #계속해서 다음 스킬 뭐 찍는지 확인

        #스택으로 만들고 앞에서부터 빼면서 순서 비교
        skill_stack = list(skill)
        while stack:
            stack_element = stack.pop(0)
            skill_stack_element = skill_stack.pop(0)
            if stack_element!= skill_stack_element:
                possible=False
                break
        if possible:
            answer+=1

    return answer


print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))
