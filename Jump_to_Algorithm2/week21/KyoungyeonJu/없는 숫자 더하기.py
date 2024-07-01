def solution(numbers):
    nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    numbers = set(numbers)

    # 두 개의 세트에서 차집합 구하기
    a = nums.difference(numbers)

    return sum(a)


"""
for문 활용하기 
    answer = 0
    for n in nums:
        if n not in numbers:
            answer += n

    return answer
"""