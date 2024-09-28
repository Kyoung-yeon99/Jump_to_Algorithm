def solution(n):
    answer = []
    # 이차원 리스트 생성(모든 요소 -1로 초기화)
    arr = []
    for i in range(1, n + 1):
        arr.append([-1] * i)
    #순회하면서 3가지 방향으로 pop 1)아래로 내려가기 2)오른쪽으로 3)왼쪽 위로
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    dirs = 0
    cur_r, cur_c = 0,0
    exit_num = 0
    for i in range(n+1):
        exit_num +=i
    cur_num = 1
    while cur_num <= exit_num:
        arr[cur_r][cur_c] = cur_num #현재 요소 answer에 저장
        cur_num+=1 #1씩 증가

        if arr:
            n_r, n_c = cur_r+dr[dirs], cur_c+dc[dirs] #다음 방향으로 이동
            if (n_r >= len(arr) and dirs == 0) or \
                    (n_c >= len(arr[cur_r]) and dirs == 1) or \
                    ((n_r < 0 and n_c < 0) and dirs == 2) or \
                    arr[n_r][n_c] > -1 :# 1)아래로 못가거나 2) 오른쪽으로 못가거나 3)왼쪽 위로 못가거나 4) 방문한 곳이면
                dirs = (dirs + 1) % 3   #방향 꺾기
                cur_r, cur_c = cur_r+dr[dirs], cur_c+dc[dirs]
            else:
                cur_r , cur_c = n_r, n_c
    return [i for row in arr for i in row]

print(solution(10))


