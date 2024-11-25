# 연산1. 문자열 뒤에 A 추가
# 연산2. 문자열 뒤에 B 추가하고 문자열 뒤집기
# S를 T로 바꿀 수 있으면 1 아니면 0

# 문자열 T에서 문자를 삭제해서 S와 비교
def solution(s, t):
    if len(s) > len(t):
        return
    if s == t:
        print(1)
        exit()

    if t[-1] == 'A':
        solution(s, t[:-1])
    if t[0] == 'B':
        t = t[1:]
        solution(s, t[::-1])

    return


S = input()
T = input()
solution(S, T)
print(0)


"""
# 시간초과
# 문자열 S에서 문자를 추가해서 T와 비교
def solution(cnt, string):
    if cnt == diff and string != T:
        return
    if string == T:
        print(1)
        exit(0)

    string_a = string + 'A'
    solution(cnt+1, string_a)
    string_b = string + 'B'
    solution(cnt+1, string_b[::-1])

    return


S = input()
T = input()
diff = len(T) - len(S)
solution(0, S)
print(0)
"""

