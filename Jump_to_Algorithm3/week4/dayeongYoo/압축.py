# LZW 과정 구현

def solution(msg):
    answer = []
    dictionary = {}

    # 알파벳 A-Z를 딕셔너리에추가 (A=1, B=2, ..., Z=26)
    for i in range(1, 27):
        # 아스키코드 to 문자열
        dictionary[chr(i + 64)] = i  # chr(65) = 'A'

    # 로직 구현
    while msg:
        idx = 0  # 마지막으로 일치한 인덱스를 저장할 변수

        # 현재 메시지의 길이 만큼 반복
        for i in range(len(msg)):
            # 현재까지의 부분 문자열이 딕셔너리에  존재하는지 확인
            if msg[:i + 1] in dictionary:
                w = msg[:i + 1]  # 현재까지의 일치하는 문자열 저장
                idx = i  # 인덱스를 업데이트

        # 일치하는 문자열의 인덱스 저장
        answer.append(dictionary[w])

        # 일치한 문자열 다음거부터 갱신
        msg = msg[idx + 1:]

        # 남은 메시지가 있는 경우
        if len(msg) > 0:
            c = msg[0]  # 다음 문자 가져오기
            # 새로운 문자열(w + c)을 딕셔너리에 추가, 다음 인덱스: 현재 크기 + 1
            dictionary[w + c] = len(dictionary) + 1

    return answer
