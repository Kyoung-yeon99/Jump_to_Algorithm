from itertools import permutations
#가능한 숫자 조합 생성 (앞에 0 고려)
#숫자 조합 리스트마다 소수 판독

def prime(n): #소수 판독 함수
    i = 2 #나누는 수
    if n<=1: #1보다 작으면 소수X
        return False

    while n>i: #소수 판독
        if n%i == 0: #나누어떨어지면 소수X, false return
            return False
        i+=1

    return True

def solution(numbers):
    answer = 0

    for l in range(1,len(numbers)+1): #자리수 1부터 n개까지의 숫자 조합 만들기
        p = set((permutations(numbers, l))) #중복되지 않는 순열 만들기 (set으로 감싸서)
        #p = (permutations(numbers, l)) #중복되지 않는 순열 만들기 (set으로 감싸서)
        for perms in p:
            if perms[0]=='0': #맨앞이 0이면 무시
                continue
            else:
                print(perms)
                num = int("".join(perms))
                result = prime(num)
                if result:
                    answer+=1
    return answer

print(solution('011'))

#테케 10번이 오래걸렸음.
# 테스트 1 〉	통과 (2.66ms, 10.3MB)
# 테스트 2 〉	통과 (225.20ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (9.10ms, 10.3MB)
# 테스트 5 〉	통과 (0.93ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.4MB)
# 테스트 7 〉	통과 (0.13ms, 10.4MB)
# 테스트 8 〉	통과 (1.00ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (3158.71ms, 10.4MB)
# 테스트 11 〉	통과 (118.14ms, 10.3MB)
# 테스트 12 〉	통과 (0.86ms, 10.3MB)
