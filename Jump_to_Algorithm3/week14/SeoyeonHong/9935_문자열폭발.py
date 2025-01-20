# 모든 폭발이 끝난 후 남은 문자열 출력
string = input()
exp = list(input()) # 폭발 문자열
l = len(exp)
result = [] # 문자열 조작이 많으므로 문자열 대신 리스트 사용

for s in string:
    result.append(s)
    if len(result) >= l and result[-l:] == exp: # 폭발 문자열일 경우
        del result[-l:] # 리스트 구간 삭제

print(''.join(result)) if result else print("FRULA")


# 시간초과
# string = input()
# exp = input()

# while exp in string:
#     string = string.replace(exp, '') # 새로운 문자열을 생성해 할당하므로 시간이 오래 걸림

# print(string) if string else print("FRULA")