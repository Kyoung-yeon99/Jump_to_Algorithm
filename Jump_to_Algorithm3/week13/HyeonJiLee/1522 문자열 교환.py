#문제 이해 -> A를 모두 연속으로 만들기?
# abab -> (aa)bb -> 모두연속, 1회
# aabbaaabaaba -> |aa)bb(aaabaaba| 에서 b와 a 교환 -> |aa)bbbb(aaaaaaaa| 로 연속임

s = input()

a_count = s.count('a')
n = len(s)
#원형 문자열이므로 앞부분 이어서 더해준 후 계산
s = s + s[:a_count - 1]
min_swaps = 1001

for i in range(n):
    #a개수만큼 윈도우 슬라이싱해서
    #b 개수 세고 (=교환 회수)
    #최소값 업데이트
    window = s[i:i + a_count]
    b_count = window.count('b')
    min_swaps = min(min_swaps, b_count)

print(min_swaps)

