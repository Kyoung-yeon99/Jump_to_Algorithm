def solution(s, skip, index):
    ans = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    # 1. skip 문자 ''으로 변환
    for sk in skip:
        alpha = alpha.replace(sk, '')

    print(alpha)

    # 2. 단어의 인덱스를 찾기
    for char in s:
        # 새로 생성한 문자리스트에서 처음 위치를 구하고 이동
        # 인덱스 에러 -> % 연산
        idx = (alpha.index(char) + index) % len(alpha)
        ans += alpha[idx]

    return ans