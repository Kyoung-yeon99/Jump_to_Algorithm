# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return
def solution(phone_book):
    phone_book.sort() # 오름차순 정렬

    for i in range(len(phone_book)-1):
        num1 = phone_book[i]
        num2 = phone_book[i+1]
        if len(num1) < len(num2) and num2[:len(num1)] == num1: # num1이 num2의 접두사일 경우
            return False
        
    return True