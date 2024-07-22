def solution(today, terms, privacies):
    t_y, t_m, t_d = map(int, today.split("."))
    answer = []
    t_dict = {}  # 약관 종류와 유효기간 딕셔너리

    for t in terms:
        alpha, month = t.split()
        t_dict[alpha] = int(month)

    for idx, p in enumerate(privacies):
        date, term = p.split()
        y, m, d = map(int, date.split("."))

        m += t_dict[term]  # 개인정보가 수집된 월에 약관 유효기간 더하기
        if m > 12:
            y += m//12  # 년에는 몫 더하기
            m %= 12  # 월은 나머지

        d -= 1
        if d == 0:  # 일이 0인 경우 처리
            m -= 1
            d = 28

        if m == 0:  # 월이 0인 경우 처리
            m = 12
            y -= 1

        today_num = t_y * 10000 + t_m * 100 + t_d
        expiry_num = y * 10000 + m * 100 + d

        if expiry_num < today_num:
            answer.append(idx + 1)

        # if y < t_y:
        #     answer.append(idx+1)
        # elif y == t_y and m < t_m:
        #     answer.append(idx + 1)
        # elif y == t_y and m == t_m and d < t_d:
        #     answer.append(idx + 1)

    return answer


"""                                                                        
# 테스트 17번 - 월이 0인 경우 처리 필요                                                                 
입력값 〉   "2020.12.28", ["A 12", "B 1"], ["2019.01.01 A", "2020.11.28 B"]    
기댓값 〉   [1, 2]                                                             
실행 결과 〉   실행한 결괏값 [1]이 기댓값 [1,2]과 다릅니다.                                    
                                                                                                                  
2020년 12월 28일 까지인데                                                         
12 / 12 의 몫을 y 에 더해 버렸고                                                    
12 % 12 를 m에 넣었기 때문이다                                                      
"""
