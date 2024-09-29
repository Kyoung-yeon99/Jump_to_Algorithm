def solution(s):
    #{} 제거, "{}", ","split, set으로 담아서
    #길이 작은것 부터 하나씩 담아가면서 원래 튜플 찾기
    s = s[:-2].replace("{","")  #맨 뒤 "}}"랑 구분자 "{" 제거
    s_list = s.split("}")   #}로 split -> , 만 남음

    arr = []
    for t in s_list:
        tmp = set(t.lstrip(",").split(",")) #set으로 담기
        arr.append(tmp)

    arr.sort(key = lambda x:len(x)) #set 길이가 작은 것부터 정렬

    answer = []
    answer.append((int((arr[0]).copy().pop()))) #맨 첫번째 요소 넣기

    for i in range(len(arr)-1):
        sub = arr[i+1] - arr[i] #뒤에 튜플에서 앞에 튜플 빼기(차집합)
        print(int(list(sub)[0]))
        answer.append(int(list(sub)[0]))

    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))