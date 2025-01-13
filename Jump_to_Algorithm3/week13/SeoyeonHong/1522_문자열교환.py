# a를 모두 연속으로 만들기 위해서 필요한 최소 교환(자리 바꿈) 횟수
string = list(input().rstrip())
min_count = len(string) # 최소 교환 횟수
a = string.count('a') # a의 총 개수
string += string[0:a-1] # 연속인 문자열(a...)의 길이 == a의 총 개수 임을 고려하여 원형 문자열 해결

for i in range (len(string)-a+1): # 원본 문자열의 길이만큼
    min_count = min(min_count, string[i:i+a].count('b')) # i~i+a번째 문자들 중 b의 개수만큼 교환해야 a를 모두 연속으로 만들 수 있음

print(min_count)