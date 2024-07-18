def solution(book_time):
    n = len(book_time)
    
    # 1. 분으로 변경 
    for i in range(n):
        in_time, out_time = book_time[i]
        in_time = in_time.split(':')
        out_time = out_time.split(':')
        
        book_time[i][0] = int(in_time[0]) * 60 + int(in_time[1])
        book_time[i][1] = int(out_time[0]) * 60 + int(out_time[1])
    
    # 2. in_time 기준으로 정렬 
    # out time 기준으로 정렬하면 중간에 빈 공간 생기면 못찾음
    # [["05:57", "06:02"], ["04:00", "06:59"], ["03:56", "07:57"], ["06:12", "08:55"], ["07:09", "07:11"]]
    # 3
    book_time.sort(key = lambda x: x[0]) 
    out = [book_time[0][1] + 10] # 퇴실 시간 등록 
    
    # 3. out 배열을 돌며 입실시간이 out 배열보다 큰지 확인 
    for i in range(1, n):
        in_time, out_time = book_time[i]
        out.sort()
        
        for idx, can_use in enumerate(out):
            # 사용 가능한 방이 있다면 
            if in_time >= can_use:
                # 방 사용 시간 갱신 
                out[idx] = out_time + 10
                break

        # 사용 가능한 방이 없다면 
        else:
            # out 추가 == 방 추가 
            out.append(out_time + 10)
    
    return len(out)
