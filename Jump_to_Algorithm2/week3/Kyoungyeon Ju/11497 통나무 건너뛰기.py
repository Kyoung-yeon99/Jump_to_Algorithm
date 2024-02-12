t = int(input())  # 테스트 케이스
for _ in range(t):
    n = int(input())  # 통나무 개수
    trees = list(map(int, input().split()))  # 통나무 높이
    trees.sort(reverse=True)  # 내림차순 정렬
    n_trees = []

    # 최소 난이도가 나오도록 정규분포 형태로 가운데에 제일 큰 수, 양쪽에 번갈아 수 배치
    for i in range(n):
        if i % 2 == 0:  # 짝수 인덱스이면 앞으로 넣고
            n_trees.insert(0, trees[i])
        else:  # 홀수 인덱스이면 뒤로 넣고
            n_trees.append(trees[i])

    level = 0  # 최소 난이도 초기화
    for i in range(n):
        if i == n-1:
            level = max(level, abs(n_trees[i] - n_trees[0]))
        else:
            level = max(level, abs(n_trees[i+1] - n_trees[i]))

    print(level)
