import sys
input = sys.stdin.readline

n = int(input())
nc = set(map(int, input().split()))  # 중복 카드가 없다고 했기 때문에 set 가능
m = int(input())
mc = list(map(int, input().split()))

for value in mc:
    if value in nc:
        print(1, end=' ')
    else:
        print(0, end=' ')


