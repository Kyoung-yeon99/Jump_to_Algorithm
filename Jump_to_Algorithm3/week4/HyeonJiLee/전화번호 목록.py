import heapq as h

def solution(phone_book):
    #정렬 안하면 return 조건을 완벽히 보장하지 않아서 틀림. 가장 짧은 번호 순서대로 추가해서 딕셔너리에 넣어야 함.
    phone_book.sort(key=lambda x:(x, len(x)))
    #문자열 정렬
    phone_book_dic = {}
    #딕셔너리에 각 전화번호 넣으면서, 해당 전화번호 문자열을 탐색
    #1. 일단 딕셔너리에 추가 ex) 119,  -> {'119':True }
    #2. 딕셔너리 내에서 '1', '11' 순회
    #3. '119'는 같으니까 continue 해서 비교 제외
    #4. 어떤 번호가 다른 번호의 접두어인 경우 return False
    for phone_number in phone_book:
        phone_book_dic[phone_number] = True #1. 일단 딕셔너리에 추가
        for i in range(1,len(phone_number)+1): #2. phone_number 길이 조절하면서 딕셔너리 순회
            prefix = phone_number[:i]
            if phone_book_dic.get(prefix): #3. 딕셔너리 순회 하다가
                if prefix == phone_number: continue # 3. 접두사 = 현재 문자열과 같으면 pass
                else:#4. 어떤 번호가 다른 번호의 접두어인 경우 return False
                    return False
    return True


print(solution(["119", "97674223", "1192", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))


# phone_book.sort(key=lambda x:(x, len(x)))
# 테스트 1 〉	통과 (6.46ms, 11.3MB)
# 테스트 2 〉	통과 (7.00ms, 11.2MB)
# 테스트 3 〉	통과 (880.57ms, 58.9MB)
# 테스트 4 〉	통과 (625.21ms, 45.4MB)

# phone_book.sort()
# 테스트 1 〉	통과 (2.78ms, 10.7MB)
# 테스트 2 〉	통과 (2.73ms, 10.8MB)
# 테스트 3 〉	통과 (814.88ms, 46.7MB)
# 테스트 4 〉	통과 (796.66ms, 34.6MB)