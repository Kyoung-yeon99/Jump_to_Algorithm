from collections import deque
N, L, R = map(int, input().split())
arr = []

dr = [-1,0,1,0]
dc = [0,1,0,-1]

for _ in range(N):
    arr.append(list(map(int,input().split())))

def dfs(r,c, visited):
    stack = deque()

    stack.append([r, c])
    union = set()
    union.add((r,c))
    while stack:
        cur_r, cur_c = stack.popleft()
        visited[cur_r][cur_c] = True
        cur_population = arr[cur_r][cur_c]

        for i in range(4): #네방향 움직이는대로
            next_r, next_c = cur_r + dr[i], cur_c + dc[i]
            if 0<=next_r < N and 0<= next_c < N and visited[next_r][next_c] is False:
                next_population = arr[next_r][next_c]
                #인구 차이가 L명 이상, R명 이하라면 이동, 방문체크도 해야 중복 탐색 방지!!
                if L<= abs(cur_population - next_population)<= R:
                    stack.append((next_r, next_c))
                    visited[next_r][next_c] = True
                    union.add((next_r, next_c))

    return union, visited

def move_pop(union):
    print(f"구한 연합: {union}")
    sum_pop = 0
    conturies = len(union)
    for cur_r, cur_c in union:
        sum_pop += arr[cur_r][cur_c]
    # 연합국가 칸의 인구수 구하기
    move_pop = sum_pop // conturies
    # 인구 이동
    for r, c in union:
        arr[r][c] = move_pop

    for a in arr:
        print(a)
    return arr

days = 0
while True:
    is_changed = False
    visited = []
    union_list = []
    for _ in range(N):
        visited.append([False]*N)
    for r in range(N):
        for c in range(N):
            if visited[r][c] == True:
                continue
            #연합 국가 탐색
            union, visited = dfs(r,c, visited)
            # print(f'현재 위치{r},{c}')
            #연합이 없으면

            if len(union) <= 1:
                continue
            #연합이 있으면
            else:
                # 연합국 추가
                is_changed = True
                union_list.append(union)

    if is_changed:
        for union in union_list:
            # 연합국간 인구 이동
            move_pop(union)
        #하루 지남
        # print("하루지남")
        days+=1
    else:
        break

print(days)
