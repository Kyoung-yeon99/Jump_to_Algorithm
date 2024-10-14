def solution(n, k):
    i = 0  # 첫번째 스택에 담아둬서 1부터 시작
    next = i+1
    num_len = len(n) - k
    stack = [n[0]]  # 맨 첫번째 숫자 담아두고 초기화
    while i + 1 < len(n):
        if len(stack) > 0 and n[next] > stack[-1]:  # 크다면 제외, 바꾸기
            while len(stack)>0 and stack[-1]<n[next] : #더 작은 숫자들은 전부 제외 -- 하면안됨!! 하다가 스택 길이가 num_len보다 작아지면 안됨
                stack.pop()
                if len(stack) + (len(n) - next) == num_len:  # 뒤에 숫자들을 다 담아야하면
                    return ''.join(stack + list(n[next:]))

            stack.append(n[next])
        elif len(stack)<num_len:  # 작거나 같으면 비교할 다음숫자에 해당. 스택에 일단 추가, 숫자 길이 확인
            stack.append(n[next])

        if len(stack) + (len(n) - next) == num_len:  # 뒤에 숫자들을 다 담아야하면
            return ''.join(stack + list(n[next:]))
            # 정해진 숫자 길이가 될때까지 나머지 뒤숫자를 다 담기

        i += 1
        next = i + 1
    return ''.join(stack + list(n[next:]))


print(solution('123454321',5))
print(solution('1924',2))
# print(solution('4177252841',4))