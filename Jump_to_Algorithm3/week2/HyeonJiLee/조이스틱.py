def solution(name):
    # str_len = len(name.rstrip('A'))  # 마지막 A는 고려하지 않은 문자열 길이
    str_len = len(name)
    name = list(map(lambda x: min(ord(x) - 65, abs(26 - (ord(x) - 65))),
                    name))  # 각 글자마다 이동해야하는 조이스틱 조작 횟수 리스트, A로부터 더 가까운 방향(위/아래)까지 고려
    move = str_len - 1  # 최대 이동 거리

    for i in range(str_len):  #오른쪽으로 계속 이동
        id = i + 1
        while id < str_len and name[id] == 0:  # i 다음에서부터 연속되는 A 자리수 구하기
            id += 1
        # print(move ,i * 2 + str_len - 1 - id,i+2*(str_len-id))
        move = min([move, i * 2 + (str_len - id), i+2 * (str_len - id)]) # i 위치에서 오른쪽으로 가는 이동 횟수 vs 왼쪽으로 돌아서 연속되는 A 끝난 후 까지 가는 이동 횟수

    return move + sum(name)


'''
#테케 모음
print(solution("ABABAAAAAAABA")) #10
print(solution("BBAABAAAAB"))  # 10
print(solution("AABAAAAAAAB")) #6
print(solution("ABBBBAAAAABAAA")) #15
print(solution("BBABA")) #6
print(solution("BBBAAB")) #8
print(solution("BBAABAA")) #7
print(solution("BBAABBB")) #10
print(solution("BBAABAAAA")) #7
print(solution("LABLPAJM")) #61
print(solution("BMOABA")) #30
print(solution("LAABAA")) #15
print(solution("AAAAAAAAJAAAA")) #14
print(solution("SAAAAAARRM")) #41
print(solution("RABAMATAWADLAFAVAAE")) #78
print(solution("XAAAAAABA")) #6
print(solution("AYOZAAVADAY")) #35
print(solution("AAFEASAAVA")) #30
print(solution("UAGAAASAAFAFXZA")) #47
print(solution("AAAAZAATAEA")) #19
print(solution("AACALATLAHABAA")) #50
print(solution("FAWJAAAFV")) #35
print(solution("AACAVAAPSAAOAA")) #49
print(solution("AWAWVAQVAAA")) #35
print(solution("RCETAAAAVUEAETZAAAK")) #75
print(solution("AAAABAAAAAAKSAIQ")) #49
print(solution("ADASAAAUAAAPAA")) #39
print(solution("AAAAADBAAELSPUAAAOA")) #70
print(solution("VJAAIAFNAAAAA")) #47
print(solution("AARUAUAAHTBJAAYS")) #69
print(solution("IASAGITUPHE")) #74
print(solution("AAALAAAAAA")) #14
print(solution("AAAEASAHQAYTAAAJ")) #60
print(solution("BAALEAAAPMAAAHSRAV")) #83
print(solution("ASWAAATDAJAXA")) #45
print(solution("DYAOAAAARQANAWA")) #66
print(solution("AAIAPB")) #24
print(solution("GTAASKKAE")) #52
print(solution("AKAAWAKX")) #33
print(solution("LOAAAHAJAAFAEBAWO")) #79
print(solution("BBAABAAAAB")) #10
'''