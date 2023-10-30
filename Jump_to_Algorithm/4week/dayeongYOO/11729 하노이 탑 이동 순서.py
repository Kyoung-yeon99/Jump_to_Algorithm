def hanoi(n, start, end):
    if n > 1:
        hanoi(n - 1, start, 6 - start - end)  # 기둥이 1개 이상이면 그룹으로 묶인 n-1개의 원판을
        # 중간으로 옮긴다
    print(start, end)

    if n > 1:
        hanoi(n - 1, 6 - start - end, end)


n = int(input())
print(2 ** n - 1)  # 2^n -1
hanoi(n, 1, 3)
