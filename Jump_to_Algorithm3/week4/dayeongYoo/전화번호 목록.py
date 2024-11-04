def solution(phone_book):
    answer = True

    # 전화번호가 다른 전화번호의 접두어인지 판단
    # 접두어인지 어캐 판단하지
    # 1.파이썬 문자열 시작 비교하는 함수 사용: startswith
    # 2.해시맵으로 해당 전화번호를 저장해두고, temp로 한문자씩 붙여서 접두어 인지 체크!

    dic = {}
    for n in phone_book:
        if n not in dic:
            dic[n] = 1  # 같은 전화번호 중복 x else 생략
    for phone in phone_book:
        tmp = ''
        for num in phone:
            tmp += num
            if tmp != phone and tmp in dic:  # 자기자신이 아니고 접두어일때
                return False

    return answer