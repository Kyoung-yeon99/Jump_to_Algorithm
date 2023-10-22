# 시간 초과....
import sys
input = sys.stdin.readline
n = int(input())


def is_pseudo(st, start, end):  # 유사회문 확인
    while True:
        if start > end: break
        if st[start] == st[end]:
            start += 1
            end -= 1
        else: return False

    return True


def is_palindrom(st):  # 팰린드롬 확인
    if st == st[::-1]:  # 팰린드롬이면 0 리턴
        return 0
    else:
        start, end = 0, len(st)-1
        while True:
            if start > end: break
            if st[start] != st[end]:
                left = is_pseudo(st, start+1, end)
                right = is_pseudo(st, start, end-1)
                if left or right: return 1
                else: return 2
            else:
                start += 1
                end -= 1


for _ in range(n):
    print(is_palindrom(input().strip()))


"""
# 시간 초과....
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    str_ = input().strip()
    start, end = 0, len(str_)-1
    count = 0
    while True:
        if start > end: break
        if str_[start] == str_[end]:  # 양쪽이 같은 문자이면
            start += 1
            end -= 1
            continue

        # 양쪽이 다른 문자이면
        if str_[start + 1] == str_[end]:  # 왼쪽에서 한 문자 건너뛰고 같은 문자이면
            tmp = str_[start + 1:end + 1]
            if tmp == tmp[::-1]:
                count = 1
                break
        elif str_[start] == str_[end - 1]:  # 오른쪽에서 한 문자 건너뛰고 같은 문자이면
            tmp = str_[start:end]
            if tmp == tmp[::-1]:
                count = 1
                break
        else:
            count = 2
            break

    print(count)
"""