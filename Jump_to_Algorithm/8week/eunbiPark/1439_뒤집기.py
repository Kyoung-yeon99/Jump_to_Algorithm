# s: 0, 1로만 이루어진 문자열
# 하나 이상 연속된 숫자를 모두 잡고 뒤집어 1 -> 0, 0 - > 1 로 변환하여 모든 수를 동일하게 만들기
# 행동의 최소 횟수 구하기

# 1 -> 0, 0 -> 1 횟수 세기
    # 1을 뒤집는 횟수
    ## 0 -> 1

    # 0을 뒤집는 횟수
    ## 1 -> 0


s= input()

turn_zero = 0
turn_one = 0

# 맨 앞 수는 확인할 수 없으니 0인지 1인지 확인해서 임의로 추가하기
if s[0] == '1':
    turn_one += 1
else:
    turn_zero += 1

for i in range(len(s)):
    if s[i:i+2] == '01':
        turn_one += 1
    elif s[i:i+2] == '10':
        turn_zero += 1

print(min(turn_zero, turn_one))
