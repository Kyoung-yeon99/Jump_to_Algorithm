# 개미 여러 마리가 길이가 l cm인 막대 위에
# 개미 이동 속도 일정, 1cm/s

# 규칙
# 개미가 막대의 마지막까지 걸어간다면, 개미는 떨어짐.
# 두 개미가 만나게 된다면 방향을 반대로

# 초기 막대에서의 개미 위치 알고있음.
# 그러나 어느 방향으로 움직이는지 모름.
# 모든 개미가 땅으로 떨어질 때까지 가능한 시간 중 빠른 시간, 느린 시간?


tc = int(input())

for t in range(tc):
    stick, n = map(int, input().split())
    ant = [int(input()) for _ in range(n)]
    # 어떻게 개미의 이동을 표현하지? - 자료구조화 고민..
    # 배열의 인덱스로?
    # nono. 1차원으로 접근할 것(막대 길이)

    # 개미의 위치를 확인하면서 오른쪽, 왼쪽 중 어디가 더 가까운가?
    # 모든 개미가 가까운쪽으로 간 경우-최소 시간, 먼쪽으로 간 경우-최대 시간
    shortest = []
    longest = []
    for a in ant:
        shortest.append(min(a, stick - a))
        longest.append(max(a, stick - a))

    print(max(shortest), max(longest))  # 모든 개미가 떨어져야 하므로 최댓값
