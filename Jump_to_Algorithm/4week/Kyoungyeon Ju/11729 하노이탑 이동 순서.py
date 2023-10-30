N = int(input())
cnt = 2 ** N - 1
print(cnt)


def Hanoi(n, s, e, m):  # n은 num, s는 start, m은 middle, e는 end
    if n == 1:  # n = 1이면 이동
        print(s, e)
        return

    # print("일반적인 상황 n =", n, "start =", s, "end =", e, "mid =", m)
    Hanoi(n - 1, s, m, e)  # n-1을 start에서 mid로 이동
    # print("첫번째 돌아온 후")
    print(s, e)  # n을 start에서 end로 이동
    Hanoi(n-1, m, e, s)  # mid로 이동한 n-1을 end로 이동
    # print("두번째 돌아온 후 ") 


Hanoi(N, 1, 3, 2)
