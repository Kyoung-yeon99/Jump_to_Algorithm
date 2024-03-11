# 0이 되는 수식 찾기
# 정렬 해서 반환
import sys
input = sys.stdin.readline
t = int(input())

def choose(num_list, n):
    if len(num_list) ==n:
        operate.append(num_list[:])
        return

    num_list.append(' ')
    choose(num_list, n)
    num_list.pop()

    num_list.append('+')
    choose(num_list, n)
    num_list.pop()

    num_list.append('-')
    choose(num_list, n)
    num_list.pop()

for _ in range(t):
    operate = []
    n = int(input())
    choose([], n-1)

    nums = [i for i in range(1, n + 1)]

    for o in operate:
        s = ''
        for i in range(n - 1):
            s += str(nums[i]) + o[i]
        s += str(nums[-1])
        if eval(s.replace(' ', '')) == 0:
            print(s)
    print()