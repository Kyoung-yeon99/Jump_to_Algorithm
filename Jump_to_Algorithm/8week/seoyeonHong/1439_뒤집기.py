# 0과 1로만 이루저니 문자열 S
# S에서 연속된 하나 이상의 숫자를 모두 뒤집기
# 최소 몇 번을 뒤집어야 모두 0 또는 1로 만들 수 있는가?
os = input() # 입력 문자열 (original string)
ns = os[0] # 새로운 문자열 (new string)

for s in os: # 연속되는 문자열은 하나의 문자로 치환
    if s != ns[-1]:
        ns += s

count = ns.count('0')
print(min(count, len(ns) - count)) # ns에서 0 또는 1의 개수 중 최솟값만큼 뒤집어야 함

