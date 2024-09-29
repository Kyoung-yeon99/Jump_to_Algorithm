from itertools import permutations as perm

def solution(expression):
    #1. 연산자별로 split해서 문자열 리스트 생성
    #2. 연산자 우선순위 조합 생성
    #3. 우선순위 루프 3개 만들어서 계산

    #문자열 돌면서 연산자는 *, +, - 기준으로 split
    result_sample = []
    num_str= ""
    expression = list(expression)
    while expression:
        char = expression.pop(0)
        if char in "*-+":
            result_sample.append(num_str)
            result_sample.append(char)
            num_str=""
        else:
            num_str+=char
        if len(expression) < 1:
            result_sample.append(num_str)
    #* 은 1, + 은 2, - 는 3 으로 매핑해서 우선순위 조합 만들기
    exp_dic = {1:"*", 2:"+", 3:"-"}
    exp_list = list(perm([1,2,3],3)) #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

    exp_result = [] #각 우선순위 연산 결과를 담을 리스트

    for exp_tuple in exp_list: #연산자 경우의수 돌면서 최댓값 구하기
        result = result_sample.copy()
        idx = 0
        #우선순위 첫번째 연산자 계산
        while idx < len(result):
            if result[idx] == exp_dic.get(exp_tuple[0]):
                eval_result = str(eval("".join(result[idx-1:idx+2])))#수식 계산
                result.pop(idx+1) #숫자 + 연산자 + 숫자 3개 지우고
                result.pop(idx) #숫자 + 연산자 + 숫자 3개 지우고
                result.pop(idx-1) #숫자 + 연산자 + 숫자 3개 지우고
                idx -= 1 #뒤로 이동
                result.insert(idx, eval_result)
            idx+=1
        idx = 0
        #우선순위 두번째 연산자 계산
        while idx < len(result):
            if result[idx] == exp_dic.get(exp_tuple[1]):
                eval_result = str(eval("".join(result[idx-1:idx+2])))#수식 계산
                result.pop(idx+1) #숫자 + 연산자 + 숫자 3개 지우고
                result.pop(idx) #숫자 + 연산자 + 숫자 3개 지우고
                result.pop(idx-1) #숫자 + 연산자 + 숫자 3개 지우고
                idx -= 1 #뒤로 이동
                result.insert(idx, eval_result)
            idx+=1
        idx = 0
        #우선순위 마지막 연산자 계산
        while idx < len(result):
            if result[idx] == exp_dic.get(exp_tuple[2]):
                eval_result = str(eval("".join(result[idx-1:idx+2])))#수식 계산
                result.pop(idx+1) #숫자 + 연산자 + 숫자 3개 지우고
                result.pop(idx) #숫자 + 연산자 + 숫자 3개 지우고
                result.pop(idx-1) #숫자 + 연산자 + 숫자 3개 지우고
                idx -= 1 #뒤로 이동
                result.insert(idx, eval_result)
            idx+=1

        exp_result.append(abs(int(result[0]))) #절댓값 저장

    return max(exp_result) # 최댓값 반환

print(solution("100-200*300-500+20"))