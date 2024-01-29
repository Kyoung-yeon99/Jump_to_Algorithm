os = input() # 처음 문자열
ns = os[0] # 새로운 문자열(시작 숫자는 같음)
for s in os:
    if s != ns[-1]: # 숫자가 바뀔 경우
        ns += s # 해당 숫자 저장
count = ns.count('0') # 새로운 문자열에 있는 0의 개수
print(min(count, len(ns) - count)) # 0 또는 1의 개수만큼 뒤집어야함을 이용