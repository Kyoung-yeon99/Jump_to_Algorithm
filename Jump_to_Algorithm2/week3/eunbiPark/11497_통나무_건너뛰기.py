t = int(input())
for _ in range(t):
    n = int(input())
    woods = list(map(int, input().split()))
    woods.sort()

    bridge = [] # 통나무 다리
    for idx, w in enumerate(woods):
        if idx % 2 == 0:
            bridge.append(w) # 뒤에 삽입
        else:
            bridge.insert(0, w) # 앞에 삽입

    maximum = abs(bridge[-1] - bridge[0]) # for 문 돌지 않는 맨 앞, 맨 뒤 계산
    for i in range(n - 1):
        maximum = max(abs(bridge[i] - bridge[i + 1]), maximum) # 최댓값 계산

    print(maximum)