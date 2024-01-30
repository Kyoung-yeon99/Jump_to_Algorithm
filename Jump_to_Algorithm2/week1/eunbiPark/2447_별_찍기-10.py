import sys
sys.setrecursionlimit(10**6)

def draw_star(n):
    if n == 1:
        return '*'

    stars = draw_star(n//3) # 이전 단계의 별의 패턴을 저장(재귀)
    result = []

    for s in stars:
        result.append(s * 3)

    for s in stars:
        result.append(s + ' ' * (n//3) + s)

    for s in stars:
        result.append(s * 3)

    return result

ans = draw_star(int(input()))
for a in ans:
    print(a)