from sys import stdin
# set difference 연산 시간 복잡도 - O(len(s) + len(t))

#차집합 함수는 쓰는 대신 아래 방법으로 적용하면 시간 복잡도 줄일 수 있음
# not in / in  시간 복잡도 - O(1)
# remove 시간 복잡도 - O(1)

N, M = map(int, stdin.readline().rstrip().split())
keyword = set()
for n in range(N):
    str = stdin.readline().rstrip()
    keyword.add(str)

for m in range(M):
    inputs = set(stdin.readline().rstrip().split(','))
    for input in inputs:
        if input in keyword:
            keyword.remove(input)
    # keyword = keyword.difference(inputs)
    print(len(keyword))
