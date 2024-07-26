# https://school.programmers.co.kr/learn/courses/30/lessons/155651

# 오답
# 최소 객실의 수
def solution(book_time):
    rooms = []

    for i in range(len(book_time)):
        start, end = book_time[i]
        sh, sm = int(start[:2]), int(start[3:])
        eh, em = int(end[:2]), int(end[3:])
        book_time[i] = [sh * 60 + sm, eh * 60 + em + 10]
        
    book_time.sort()
    
    for time in book_time:
        assigned = False
        for room in rooms:
            if room[1] <= time[0]:
                room = time
                assigned = True
                break
        if not assigned:
            rooms.append(time)
        
    return len(rooms)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))