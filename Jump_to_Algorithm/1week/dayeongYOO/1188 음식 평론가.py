import sys

input = sys.stdin.readline

meat, person = map(int, input().split())
ans = 0  # 개수

def cut(a, b):
    if b==0:
        return a
    return cut(b, a%b)

print(person-cut(meat, person))