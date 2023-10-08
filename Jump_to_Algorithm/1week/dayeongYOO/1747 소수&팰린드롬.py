import sys

input = sys.stdin.readline


def pal(word):  # 팰린드롬 판정
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return pal(word[1:-1])


def prime(number):  # 소수판정
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


start, end = map(int, input().split())

if end > 10000000:  # 천만 넘는 팰린드롬 없음
    end = 10000000

li = []
for i in range(start, end + 1):
    i = str(i)
    if pal(i) == True:  # 팰린드롬이면 리스트에 넣기
        li.append(int(i))

for num in li:
    if prime(num) == True:  # 리스트 중 소수이면 출력
        print(num)

print(-1)
