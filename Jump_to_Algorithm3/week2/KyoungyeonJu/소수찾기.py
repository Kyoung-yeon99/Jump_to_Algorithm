from itertools import permutations
import math


def solution(numbers):
    def is_prime_number(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    answer = 0
    a = set()

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            num = int(''.join(j))
            print(j, num, answer)
            if num > 1 and num not in a:
                if is_prime_number(num):
                    answer += 1
                a.add(num)

    return answer