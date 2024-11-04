def 진수변환(i, n):
    n_number = ''
    alpha_dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    if i==0: return '0'
    while i>0:
        n_number += str(i % n) if i%n < 10 else alpha_dic[i%n]
        i //=n

    return n_number[::-1]

def solution(n, t, m, p):
    numbers = ''
    i = 0
    while len(numbers)<t*m: #미리 구할 숫자 개수만큼 loop 돌기
        numbers += str(진수변환(i,n))
        i+=1

    return numbers[p-1:t*m:m]

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))