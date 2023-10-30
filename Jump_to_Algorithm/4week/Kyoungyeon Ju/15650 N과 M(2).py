N, M = map(int, input().split())
result = []

# for문의 start를 함수로 넘겨주는 방법
# 시간 40ms
def backTracking(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(start, N+1):
        print("i =", i)
        if i not in result:
            print(i,"not in result and result=", result)
            result.append(i)
            backTracking(i+1)
            result.pop()
            print("pop out, i =", i, result)


backTracking(1)


"""
# 리스트 자체를 함수로 넘기고 for문 안의 조건문에서 길이 조건과 오름차순 조건 확인
# 시간 53ms
def backTracking(result):
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N+1):
        if i not in result and (len(result) == 0 or i > result[-1]):
            result.append(i)
            backTracking(result)
            result.pop()


backTracking(result)




# visited 리스트 활용, 시간 40ms
visited = [False]*(N+1)


def backTracking():
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N+1):
        if (visited[i] == False) and (len(result) == 0 or i > result[-1]):
            visited[i] = True
            result.append(i)
            backTracking()
            visited[i] = False
            result.pop()


backTracking()
"""

