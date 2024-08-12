
def solution(arrayA, arrayB):
    # 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a 구하기, 없으면 0 return
    # 조건1. 철수 숫자 모두 나누기 가능, 영희 숫자 하나도 나누기 X
    # 조건2. 영희 숫자 모두 나누기 가능, 철수 숫자 하나도 나누기 X
    def get_gcd(a, b):
        if a % b == 0:
            return b
        return get_gcd(b, a % b)

    def find_gcd(array):
        gcd = 0
        for i in range(len(array)):
            gcd = get_gcd(gcd, array[i])
        return gcd

    def check_gcd(gcd, array):
        for i in array:
            if i % gcd == 0:
                return False
        return True

    a_gcd, b_gcd = find_gcd(arrayA), find_gcd(arrayB)
    a_check, b_check = check_gcd(a_gcd, arrayB), check_gcd(b_gcd, arrayA)

    if not a_check and not b_check:
        return 0
    elif a_check and b_check:
        return max(a_gcd, b_gcd)
    elif a_check:
        return a_gcd
    elif b_gcd:
        return b_gcd