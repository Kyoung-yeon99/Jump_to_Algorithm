def solution(numbers):
    numbers = list(map(str,numbers))
    # 원소가 최대 1000이므로 4를 곱해서 앞자리만의 수만 비교하여 내림차순 정렬
    numbers.sort(key=lambda x: x*4, reverse=True)

    return str(int(''.join(numbers)))  # 요소가 모두 0인 경우, 0