def solution(topping):
    # 각 조각에 동일한 가짓수의 토핑이 올라가야 공평하게 나눈 것!
    # 롤케이크를 공평하게 자르는 방법의 수를 return

    answer = 0

    # 앞에서부터 토핑 가짓수, 뒤에서부터 토핑 가짓수 구하기
    front, f, back, b = [], set(), [], set()
    l, s = len(topping), len(set(topping))  # 토핑 길이, 토핑 종류 개수
    for i in range(l):
        f.add(topping[i])
        b.add(topping[l-i-1])
        front.append(len(f))
        back.append(len(b))

    back = back[::-1]

    for i in range(s//2 - 1, l-s//2):  # [토핑 종류 개수의 절반]부터, [전체 길이 - 토핑 종류 개수의 절반]까지
        if front[i] == back[i+1]:
            answer += 1

    return answer