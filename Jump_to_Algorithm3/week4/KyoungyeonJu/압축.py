def solution(msg):
    answer = []
    dict, num = {}, 27
    for i in range(65, 91):  # 길이가 1인 모든 단어 포함하도록 사전 초기화
        dict[chr(i)] = i - 64

    i = 0
    while i < len(msg):
        m, l = msg[i], 1
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기
        while i+l < len(msg) and msg[i:i+l+1] in dict:
            m = msg[i:i+l+1]
            l += 1
        if i+l >= len(msg):
            answer.append(dict[m])
            break
        answer.append(dict[m])  # 색인 번호 출력
        dict[msg[i:i+l+1]] = num  # w+c 사전 등록
        num += 1
        i += l

    return answer