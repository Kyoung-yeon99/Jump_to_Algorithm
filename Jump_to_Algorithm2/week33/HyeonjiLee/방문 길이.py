def solution(dirs):
    dir_dic = {"U":[-1,0],
               "D":[1,0],
               "L":[0,-1],
               "R":[0,1]}
    dir_list = []
    for dir in dirs:
        dir_list.append(dir_dic.get(dir))

    cur_r, cur_c = 5,5
    visited = set()
    answer = 0

    for dir in dir_list: #순서대로 움직이면서 이동한 좌표에 1씩 더해서 방문처리
        next_r = cur_r + dir[0]
        next_c = cur_c + dir[1]

        if next_r<0 or next_r > 10 or next_c<0 or next_c>10: #범위 벗어나면 처음부터
            continue

        if (cur_r,cur_c,next_r,next_c) not in visited and (next_r, next_c, cur_r, cur_c) not in visited: #set에 양쪽 방향으로 좌표 저장, 왔던 길인지 검사
            visited.add((cur_r, cur_c, next_r, next_c))
            visited.add((next_r,next_c, cur_r, cur_c))
            answer+=1

        cur_r = next_r
        cur_c = next_c

    return answer

# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
print(solution("UUUUUDDDDDDDDDD"))