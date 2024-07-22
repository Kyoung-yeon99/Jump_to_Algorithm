def solution(numbers):
    answer = -1
    num = set(numbers)
    check = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    no = check - num
    answer = sum(no)

    return answer