# https://school.programmers.co.kr/learn/courses/30/lessons/154539

# 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열
def solution(numbers):
    N = len(numbers)
    stack = []
    answer = [-1] * N
    
    for i in range(N):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
            print(stack)
        stack.append(i)
        print(stack)

    return answer


# 시간초과
# def solution(numbers):
#     answer = []
#     N = len(numbers)
#     for i in range(N):
#         cur = numbers[i]
#         for j in range(i+1, N):
#             if cur < numbers[j]:
#                 answer.append(numbers[j])
#                 break
#         if len(answer) == i:
#             answer.append(-1)
#     return answer