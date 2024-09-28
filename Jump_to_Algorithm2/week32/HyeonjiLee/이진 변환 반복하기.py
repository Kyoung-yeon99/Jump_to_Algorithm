def solution(s):
    count, zero = 0,0
    while s != '1':
        #0 카운트, 0 제거
        zero += s.count('0')
        s = s.replace('0','')

        # 2진수 변환 ex)0b110 -> b 구분자로 split해서 110 가져옴
        s = str(bin(len(s))).split('b')[-1]

        count +=1

    return [count, zero]

print(solution('110010101001'))
print(solution('01110'))
print(solution('1111111'))
