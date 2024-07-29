def solution(numbers):
    n = len(numbers)
    answer = [-1 for _ in range(n)]
    stack = [] # 인덱스 등록
    
    for i in range(n):
        # 뒷 수의 역할을 할 수 있는지 판단 
        # 스택에 값이 있고 스택 맨 위 값이 가리키는 값이 현재 값 보다 작다면 
        while stack and numbers[stack[-1]] < numbers[i]:
            # 뒷수의 역할을 할 수 있음
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer
