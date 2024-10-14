def solution(p, l):
    # 보트에 사람을 태우고 난 남은 무게가 최소가 되도록 해야 함!
    p.sort()  # 크기순으로 정렬하고 뒤집기 [80,70,50,50]
    p.reverse()
    boat_num = 0
    i = 0
    back = len(p) - 1
    while i <= back :  # 모든 사람을 다 태울 때까지
        # 남은 한 명을 누구를 태울 것 인가?->그다음으로 무거운 사람 or 맨 뒤 가벼운사람
        if l - p[i] < p[back]:  # 더 태울 수 없다면
            # print(i, back, p[i], p[back], boat_num, '1')
            i += 1  # 혼자 먼저 보내기. 다음 인덱스로 이동
            boat_num += 1
        elif i+1<len(p) and l - p[i] - p[i + 1] >= 0:  # 그 다음으로 무거운 사람 먼저 확인/태울 수 있으면
            # print(i, back, p[i], p[back], boat_num,'2')
            i += 2  # 두명 보내서 인덱스 +2 하기
            boat_num += 1
        elif l - p[i] >= p[back]:  # 그다음으로 제일 가벼운사람 태울 수 있다면
            # print(i, back, p[i], p[back], boat_num,'3')
            i += 1
            back -= 1
            boat_num += 1

    return boat_num
print(solution([70, 80, 50],100))
# print(solution([40,40,40,40,60,90,100,70, 50, 80, 50],100))
