def solution(numbers):
    # 길이
    n = len(numbers)

    # 결과 저장 배열
    # 모든 원소에 대해 뒷 큰수가 없다고 가정하고 -1로 초기화
    answer = [-1] * (n)

    # 스택을 사용해 배열 탐색->중복 비교 제거&효율적 탐색
    # 스택에는 현재 원소보다 큰 값들을 저장
    stack = []

    # 배열을 뒤에서 앞으로 탐색
    for i in range(n - 1, -1, -1):
        while stack:
            idx = stack[-1]

            # 스택 꼭대기 값이 현재 값보다 크다면 -> 결과 업데이트
            if numbers[idx] > numbers[i]:
                answer[i] = numbers[idx]  # 결과 업데이트
                break  # continue 아니고 break 주의(while까지 탈출하도록)

            # 스택 꼭대기 값이 현재 값보다 작거나 같다면 -> 스택에서 꺼냄
            elif numbers[stack[-1]] <= numbers[i]:
                stack.pop()

        # 스택에 현재 인덱스 추가
        stack.append(i)

    return answer
