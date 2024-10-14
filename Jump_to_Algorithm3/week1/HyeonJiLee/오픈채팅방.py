def solution(record):
    uid_dic = {} #uid : 닉네임 딕셔너리
    orders_dic = {'Enter': '님이 들어왔습니다.', #입퇴장 문자열 매핑 딕셔너리
                  'Leave': '님이 나갔습니다.'}
    orders = []
    for r in record:
        str_list = r.split() #입퇴장, uid, 닉네임 분리
        if str_list[0]=='Change' or str_list[0] =='Enter': #이름 바꿨거나 입장하면 닉네임 업데이트
            uid_dic[str_list[1]] = str_list[2]

        if str_list[0] == 'Leave' or str_list[0] == 'Enter': #입퇴장 기록하기
            orders.append([str_list[0],str_list[1]])

    answer = []

    for enter_leave,uid in orders: #입퇴장 기록 보면서 문자열 매핑하기
        answer.append(uid_dic[uid]+orders_dic[enter_leave])

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))