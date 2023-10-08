# 에라토스테네스의 체
n, k = map(int, input().split())
num_list = list(range(2, n + 1))
rm = 0  # 지워지는 수의 개수
breaker = False

while len(num_list) > 0:
    a = num_list[0]  # 리스트에서 가장 작은 수
    eol = num_list[-1] // a  # 가장 큰 수 // 가장 작은 수 몫 계산

    for i in range(1, eol + 1):
        number = a * i  # 지워지는 수
        try:  # 리스트 안에 값이 없는 경우 예외처리
            num_list.remove(number)
            rm += 1
        except:
            pass
        if rm == k:  # k번째 지워지는 수
            breaker = True  # for문 탈출
            break
    # while문 탈출
    if breaker:
        break

print(number)
