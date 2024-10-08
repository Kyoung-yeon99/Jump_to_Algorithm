def solution(numbers, target):
    def f(i, s):
        nonlocal answer

        if i == len(numbers):
            if s == target:
                answer += 1
            return

        f(i + 1, s + numbers[i])
        f(i + 1, s - numbers[i])

    answer = 0
    f(0, 0)

    return answer
