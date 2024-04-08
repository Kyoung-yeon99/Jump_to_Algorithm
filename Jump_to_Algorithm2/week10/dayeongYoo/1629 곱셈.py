# https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-1629-%EA%B3%B1%EC%85%88-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5-%EB%AA%A8%EB%93%88%EB%9F%AC-%EC%97%B0%EC%82%B0-%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98


a, b, c = map(int, input().split())


def power(n):
    if n == 0:
        return 1  # n이 0이면 1을 반환한다.
    if n % 2 == 0:
        return (power(n // 2) ** 2) % c  # n이 짝수면 power(n//2)의 제곱을 반환한다.
    # n이 홀수면 power(n//2)의 제곱에 a를 곱한 값을 반환한다.
    return ((power(n // 2) ** 2) * a) % c


print(power(b))