# 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다
# 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1
# n명의 각 덩치 등수를 계산하여 출력

def get_number(w, h):
    num = 0
    for ww, hh in people:
        if w < ww and h < hh:
            num += 1
    return num + 1


n = int(input())
people = []
for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

for i in range(n):
    print(get_number(people[i][0], people[i][1]), end=" ")
